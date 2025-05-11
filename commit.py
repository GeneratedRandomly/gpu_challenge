import argparse
import os

parser = argparse.ArgumentParser(description="Commit changes to a Git repository.")
parser.add_argument(
    "-t",
    "--to",
    type=str,
)
to = parser.parse_args().to
if to == "fp8":
    os.system(
        "/opt/glibc-2.39/lib/ld-linux-x86-64.so.2 --library-path /opt/glibc-2.39/lib:/usr/lib/x86_64-linux-gnu ./popcorn-cli submit problems/amd/fp8-mm/submission.py"
    )
elif to == "moe":
    os.system(
        "/opt/glibc-2.39/lib/ld-linux-x86-64.so.2 --library-path /opt/glibc-2.39/lib:/usr/lib/x86_64-linux-gnu ./popcorn-cli submit problems/amd/moe/submission.py"
    )
elif to == "id":
    os.system(
        "/opt/glibc-2.39/lib/ld-linux-x86-64.so.2 --library-path /opt/glibc-2.39/lib:/usr/lib/x86_64-linux-gnu ./popcorn-cli submit problems/amd/identity/submission.py"
    )
