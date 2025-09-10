import sys

# Total number of pages in our graph.
TOTAL_PAGES = 8.0
INITIAL_RANK = 1.0 / TOTAL_PAGES

def main():
    for line in sys.stdin:
        source_page, out_links_str = line.strip().split('\t', 1)
        print(f"{source_page}\t{INITIAL_RANK},{out_links_str}")

if __name__ == "__main__":
    main()