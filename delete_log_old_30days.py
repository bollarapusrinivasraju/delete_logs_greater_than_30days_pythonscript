import os
from datetime import datetime as dt
from glob import glob

# Setup
path = '/tmp/logs/'  # Directory containing the files
days = 30            # Number of days to determine old files
ndays = dt.now().timestamp() - days * 86400  # Calculate timestamp for 30 days ago

# Collect all files
files = glob(os.path.join(path, '*.sql.gz'))  # Match files with .sql.gz extension
# Choose files to be deleted
to_delete = (f for f in files if os.stat(f).st_mtime < ndays)

# Delete files older than 30 days
for f in to_delete:
    os.remove(f)
    print(f"Deleted: {f}")
