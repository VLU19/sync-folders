import shutil
from pathlib import Path
from logger import get_logger


def sync_folders(source, replica, log_file_name):
    sync_folders_log = get_logger("compare_folders", log_file_name)

    source = Path(source)
    replica = Path(replica)

    if not source.exists():
        source.mkdir(parents=True)
        sync_folders_log.info(f"{source} was created!")

    if not replica.exists():
        replica.mkdir(parents=True)
        sync_folders_log.info(f"{replica} was created!")

    for item in source.glob('*'):
        if not item.is_file():
            sync_folders_log.info(f"{item} is not a file. Change it or remove from {source}!")
            continue

        replica_entry = replica / item.name
        if not replica_entry.exists() or replica_entry.stat().st_mtime < item.stat().st_mtime:
            shutil.copy2(item, replica_entry)
            sync_folders_log.info(f"Copied {item} to {replica_entry}")

    for item in replica.glob('*'):
        source_entry = source / item.name
        if not source_entry.exists():
            item.unlink()
            sync_folders_log.info(f"{source_entry} doesn't exist. Remove from {item}")
