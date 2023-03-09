import sys
import time
from sync import sync_folders

if __name__ == '__main__':
    source_folder = sys.argv[1]
    replica_folder = sys.argv[2]
    sync_interval = int(sys.argv[3])
    log_file_name = sys.argv[4]

    while True:
        sync_folders(source_folder, replica_folder, log_file_name)
        time.sleep(sync_interval)
