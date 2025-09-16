# BIG-DATA
LAB CODES ONLY

[16/09, 10:37] Yashwanth(G) Ai&Ds: # Bigram Count using Hadoop MapReduce

## Aim
To implement a MapReduce program that counts the frequency of bigrams (pairs of consecutive words) in a text dataset.

---

## Algorithm

### Mapper
1. Read each line from the input.
2. Split the line into words.
3. For each consecutive word pair (bigram), emit `(bigram, 1)`.

### Shuffle & Sort (Hadoop)
- Groups identical bigrams together across all mapper outputs.

### Reducer
1. For each bigram key, sum up the counts from all mappers.
2. Output `(bigram, total_count)`.

---

## Result
The program successfully generates all unique bigrams with their occurrence counts.  

**Example**  
Input:
[16/09, 10:38] Yashwanth(G) Ai&Ds: # Coolest Year using Hadoop MapReduce

## Aim
To implement a MapReduce program that finds the coolest year (the year with the lowest average temperature) from a dataset of yearly temperature records.

---

## Algorithm

### Mapper
1. Read each line of the dataset.
2. Extract the year from the date field.
3. Extract the temperature value and validate it.
4. Emit `(year, temperature)`.

### Shuffle & Sort (Hadoop)
- Groups all temperature values by year across mapper outputs.

### Reducer
1. For each year, compute the average of all temperature values.
2. Keep track of the year with the lowest average temperature.
3. Output the coolest year along with its average temperature.

---

## Result
The program successfully identifies the **coolest year** from the dataset.  

**Example**  
Input:
[16/09, 10:38] Yashwanth(G) Ai&Ds: # Bloom Filter using Python

## Aim
To implement a Bloom Filter algorithm using multiple hash functions, and to evaluate its performance in terms of collisions and error rates.

---

## Algorithm

### Hash Functions
- Define multiple hash functions (e.g., h1, h2, h3) that map input values to positions in a bit array.

### Bloom Filter Construction
1. Initialize a bit array of size `n` with all zeros.
2. For each input element:
   - Apply all hash functions.
   - Set the corresponding bit positions in the array to 1.
   - Count collisions when a bit is already set.
3. Return the final bit array and the number of collisions.

### Error Rate Calculation
1. Use the formula:
[16/09, 10:38] Yashwanth(G) Ai&Ds: # Distinct Email Estimation using Flajolet–Martin Algorithm

## Aim
To implement the Flajolet–Martin probabilistic algorithm for estimating the number of distinct email addresses using hash functions and trailing zeros in binary representation.

---

## Algorithm

1. **Input**  
   - Read a list of email addresses.

2. **Preprocessing**  
   - Convert each email into a decimal value by summing the ASCII values of its characters.

3. **Hashing**  
   - Apply two different hash functions (`hash1`, `hash2`) to each decimal value.

4. **Trailing Zeros**  
   - Count the number of trailing zeros in the binary form of each hash output.  
   - Keep track of the maximum number of trailing zeros (`R1`, `R2`) for each hash function.

5. **Estimation**  
   - Estimate the number of distinct emails as:  
     ```
     Estimated Count = 2^R
     ```
     where `R` is the maximum trailing zero count.

6. **Error Rate Calculation**  
   - Error is computed as:  
     ```
     Error = 1 - exp(-m * 2^(-R))
     ```
     where `m` = total number of emails.

7. **Comparison**  
   - Compare the error rates of the two hash functions and report which one performs better.

---

## Result
The program produces:  
- The **decimal values** of emails.  
- The **actual number of unique emails**.  
- The **estimated distinct count** for each hash function.  
- The **error rates** for both functions.  
- The **better hash function** based on lower error.

**Example Output** (for sample input):
[16/09, 10:38] Yashwanth(G) Ai&Ds: # PageRank using Hadoop MapReduce

## Aim
To implement the PageRank algorithm using the MapReduce paradigm, in order to calculate the importance of web pages based on their link structure.

---

## Algorithm

### Step 1: Graph Construction
1. Read input where each line contains a source page followed by its outlinks.
2. Emit the **source page** and its adjacency list (comma-separated).

### Step 2: Initialization
1. Assign an initial rank to each page:

# PageRank using Hadoop MapReduce

## Aim
To implement the PageRank algorithm using the MapReduce paradigm, in order to calculate the importance of web pages based on their link structure.

---

## Algorithm

### Step 1: Graph Construction
1. Read input where each line contains a source page followed by its outlinks.
2. Emit the **source page** and its adjacency list (comma-separated).

### Step 2: Initialization
1. Assign an initial rank to each page:

INITIAL_RANK = 1 / TOTAL_PAGES

2. Emit the page along with its initial rank and adjacency list.

### Step 3: Iterative Rank Calculation (not shown fully in this snippet)
1. For each page, distribute its rank equally among its outlinks.  
2. Apply the PageRank formula with a damping factor `d` (commonly 0.85):

PR(p) = (1 - d)/N + d * Σ (PR(q)/L(q))

where:
- `N` = total number of pages  
- `PR(q)` = rank of page `q` linking to `p`  
- `L(q)` = number of outlinks from `q`
3. Repeat until convergence or for a fixed number of iterations.

---

## Result
The program prepares data for the PageRank algorithm by:  
- Constructing the adjacency list of pages.  
- Assigning initial ranks to each page.  

**Example Input**

A B C B C C A D C

**After Step 1 (Adjacency List)**

A   B,C B   C C   A D   C

**After Step 2 (Initialization, assuming 4 pages)**

A   0.25,B,C B   0.25,C C   0.25,A D   0.25,C

These outputs are then used in the iterative PageRank calculation to determine the final ranks of all pages.
