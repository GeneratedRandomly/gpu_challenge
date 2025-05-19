#!POPCORN leaderboard amd-fp8-mm
import torch
from task import input_t, output_t

def custom_kernel(data: input_t) -> output_t:
    """
    优化版 block-scale fp8 gemm
    """
    a, b, a_scale, b_scale, c = data
    m, k = a.shape
    n = b.shape[0]
    block_k = 128
    block_n = 128

    # 输出清零
    c.zero_()

    # 按块处理
    for bk in range(0, k, block_k):
        k_len = min(block_k, k - bk)
        # 当前k块的缩放索引
        a_scale_block = a_scale[:, bk // block_k].unsqueeze(1)  # [m, 1]
        for bn in range(0, n, block_n):
            n_len = min(block_n, n - bn)
            # b块的缩放索引
            b_scale_val = b_scale[bn // block_n, bk // block_k]
            # 取出a和b的子块
            a_blk = a[:, bk:bk + k_len].to(torch.float32) * a_scale_block
            b_blk = b[bn:bn + n_len, bk:bk + k_len].to(torch.float32) * b_scale_val
            # GEMM并累加
            c[:, bn:bn + n_len] += (a_blk @ b_blk.T).to(torch.bfloat16)

    return c