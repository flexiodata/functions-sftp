
# ---
# name: sftp-import
# deployed: true
# title: SFTP Import
# description: Loads data from SFTP into indices
# ---

# main function entry point
def flex_handler(flex):
    files = flex.vars['files']
    flex.end(files)

