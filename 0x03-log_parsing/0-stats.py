import sys

"""
A script that reads stfin line by line
"""

total_fs = 0
status_code = {}

def line_parse(line):
	"""
	Parses a log line and returns file size
	"""

	try:
		_, _, _, _, _, status_code_str, file_size_str = line.split(" ", 5)
		status_code = int(status_code_str)
        fs = int(fs_str)
        return file_size
	except ValueError:
		return None

def update_mertrics(fs):
	"""
	updates total fs
	"""
	global total_fs, status_code_cnt
	total_fs += fs
	if str(fs) in status_code_cnt:
		status_code_cnt += fs
	if str(fs) in status_code_cnt:
		status_code_cnt[str(fs)] += 1
	else:
		status_code_cnt[str(fs)] = 1

def print_stats():
	"""
    Prints the current statistics.
    """
	print(f"Total file size: File size: {total_fs}")
    for status_code, cnt in sorted(status_code_cnt.items()):
        print(f"{status_code}: {cnt}")

try:
    for i, line in enumerate(sys.stdin.readlines(), start=1):
        fs = parse_line(line)
        if fs is not None:
            update_metrics(fs)
        if i % 10 == 0 or i == len(sys.stdin.readlines()):
except KeyboardInterrupt:
    print_statistics()
