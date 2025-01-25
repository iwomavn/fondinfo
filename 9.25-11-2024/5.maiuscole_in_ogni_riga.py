def process_file(filename: str):
    total_upper = 0  
    total_chars = 0 
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()  
            
            num_upper = sum(1 for char in stripped_line if char.isupper()) 
            num_total = len(stripped_line)
            
            if num_total > 0: 
                percent_upper_line = (num_upper / num_total) * 100
                print(f"Percentuale di maiuscole nella riga: {percent_upper_line:.2f}%")
            
            total_upper += num_upper  
            total_chars += num_total
    
    if total_chars > 0:  
        percent_upper_file = (total_upper / total_chars) * 100  
        print(f"\nPercentuale complessiva di maiuscole nel file: {percent_upper_file:.2f}%")
    else:
        print("Il file è vuoto o non contiene caratteri.")

process_file('../uni_python/9.25-11-2024/license.txt')