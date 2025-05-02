#  main.py
import os
from reviewer import review_iac_code

def main():
    pass
    path = "test_data\cf.yaml"
    output_path = "output\cf_improvements.txt"

    if not os.path.exists(path):
        print(f"Path does not exist{path}\n")
        return 
    
    with open(path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    reviewed_code = review_iac_code(code, model = "deepseek-r1:1.5b")

    # print the result
    print("##___OUTPUT FROM LLM___##")
    print(reviewed_code)

    # save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path,'w', encoding='utf-8') as file:
        file.write(reviewed_code)

    print(f"Reviewed code and saved output to {output_path}")

if __name__ == "__main__":
    main()