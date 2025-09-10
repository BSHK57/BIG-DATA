import sys

def main():
    """
    Mapper for the iterative PageRank calculation (Job 2).
    Input: <PageID>\t<Rank>,<Outlink1>,<Outlink2>...
    """
    for line in sys.stdin:
        page_id, data = line.strip().split('\t', 1)
        
        # --- FIX IS HERE ---
        # Split the 'data' part by the first comma to correctly separate rank from links.
        try:
            rank_str, out_links_str = data.split(',', 1)
        except ValueError:
            # This handles lines that might not have out-links (e.g., "E\t0.125,")
            rank_str = data.rstrip(',')
            out_links_str = ""
        current_rank = float(rank_str)
        out_links = out_links_str.split(',') if out_links_str else []
        out = ','.join(out_links)
        # --- END OF FIX ---

        # 1. Pass along the graph structure
        # Re-join the original out_links to preserve the structure
        print(f"{page_id}\t|{out}")

        # 2. Distribute rank to out-links
        if out_links:
            num_out_links = len(out_links)
            if num_out_links > 0:
                rank_contribution = current_rank / num_out_links
                for link in out_links:
                    if link: # Ensure the link is not an empty string
                        print(f"{link}\t{rank_contribution}")

if __name__ == "__main__":
    main()