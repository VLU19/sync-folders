## Sync Folders

- Synchronizes two folders: source and replica. The
program maintain a full, identical copy of source folder at replica folder.

- Synchronization is one-way: after the synchronization, content of the
replica folder should be modified to exactly match content of the source
folder.
- Folder paths, synchronization interval and log file path need to be provided
using the command line arguments;

```bash
python3 main.py path/to/source path/to/replica 15 path/to/logs.txt 
```

- `path/to/source` - path to source folder
- `path/to/replica` - path to replica folder
- `15` - synchronization interval
- `logs.txt` or `path/to/logs.txt` - log file path