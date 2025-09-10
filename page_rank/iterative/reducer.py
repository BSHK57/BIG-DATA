import sys

DAMPING_FACTOR = 0.85

def main():
    current_page = None
    total_rank_contribution = 0.0
    adjacency_list = ""

    for line in sys.stdin:
        page_id, value = line.strip().split('\t', 1)

        if current_page and current_page != page_id:
            # Process the completed page
            new_rank = (1 - DAMPING_FACTOR) + (DAMPING_FACTOR * total_rank_contribution)
            print(f"{current_page}\t{new_rank},{adjacency_list}")

            # Reset for the next page
            current_page = page_id
            total_rank_contribution = 0.0
            adjacency_list = ""
        
        if not current_page:
            current_page = page_id

        # Process the value
        if value.startswith('|'):
            adjacency_list = value[1:]
        else:
            total_rank_contribution += float(value)

    # Output the last page
    if current_page:
        new_rank = (1 - DAMPING_FACTOR) + (DAMPING_FACTOR * total_rank_contribution)
        print(f"{current_page}\t{new_rank},{adjacency_list}")

if __name__ == "__main__":
    main()