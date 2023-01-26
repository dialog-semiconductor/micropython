import os
from zephyr import FlashArea
bdev = FlashArea(FlashArea.STORAGE, 4096)
os.VfsLfs2.mkfs(bdev)
os.mount(bdev, '/flash')