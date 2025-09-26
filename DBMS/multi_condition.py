import re

def nlq_to_sql(nl_query):
    nl_query = nl_query.lower()
    sql = "SELECT * FROM students WHERE "
    conditions = []

   
    if "marks" in nl_query:
        if "above" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"marks > {number[0]}")
        elif "below" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"marks < {number[0]}")
        elif "equal" in nl_query or "equals" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"marks = {number[0]}")

    if "age" in nl_query:
        if "above" in nl_query or "older than" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"age > {number[0]}")
        elif "below" in nl_query or "younger than" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"age < {number[0]}")
        elif "equal" in nl_query or "equals" in nl_query:
            number = re.findall(r'\d+', nl_query)
            if number:
                conditions.append(f"age = {number[0]}")

   
    if "grade" in nl_query:
        grades = re.findall(r"grade\s*[a-z]", nl_query)
        if grades:
            grade_value = grades[0].split()[-1].upper()
            conditions.append(f"grade = '{grade_value}'")

    
    if " and " in nl_query:
        sql += " AND ".join(conditions)
    elif " or " in nl_query:
        sql += " OR ".join(conditions)
    else:
        sql += " AND ".join(conditions)  

   
    if not conditions:
        sql = "SELECT * FROM students;"

    return sql



if __name__ == "__main__":
    print("Natural Language to SQL Converter (V2: Multi-Condition Queries)")
    print("Examples:")
    print("- Show all students with marks above 80")
    print("- List students older than 20 and with grade A\n")

    user_query = input("Enter your query: ")
    sql_query = nlq_to_sql(user_query)
    
    print("\nGenerated SQL Query:")
    print(sql_query)