import sys
def main():
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) < 1:
            continue
       
        source_page = parts[0]
        out_links = parts[1:]
       
        # Emit the source page and its adjacency list as a comma-separated string
        print(f"{source_page}\t{','.join(out_links)}")

if __name__ == "__main__":
    main()