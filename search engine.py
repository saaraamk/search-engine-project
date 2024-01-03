
def get_user_query():
    """
    Gets user query as input and returns it.

    Returns:
    str: The user's search query.
    """
    user_query = input("Please enter your search query: ")
    return user_query


import os
def read_files():
    """
    Reads files in the specified directory and returns their content.

    Returns:
    dict: A dictionary containing file names as keys and file contents as values.
    """
    files_content = {}
    files = os.listdir('C:\\Users\\Sara\\Desktop\\archive\\dickens')
    for file in files:
        with open(file, 'r', encoding = "utf8") as f:
            content = f.read()
            files_content[file] = content
    return files_content


def search_query(user_query, files_content):
    """
    Reads files in the specified directory and returns their content.

    Returns:
    dict: A dictionary containing file names as keys and file contents as values.
    """
    results = []
    for file, content in files_content.items():
        lines = content.split('\n')
        for line_num, line in enumerate(lines, start=1):
            words = line.split()
            for word in words:
                if user_query.lower() == word.lower():
                    result = {
                        'File': file,
                        'Line': line_num,
                        'Text': line
                    }
                    results.append(result)
                    break
    return results


def search_query_multi_words(user_query, files_content):
    """Searches for a multi-word user query within the content of multiple files.

    Args:
        user_query (str): The multi-word query entered by the user.
        files_content (dict): A dictionary containing file names as keys and their corresponding content as values.

    Returns:
        list: A list of dictionaries representing the search results. Each dictionary contains the 'File' name, 
        'Line' number, and 'Text' line that matches the user query."""
    
    results = []
    for file, content in files_content.items():
        lines = content.split('\n')
        for line_num, line in enumerate(lines, start=1):
            if user_query.lower() in line.lower():
                result = {
                    'File': file,
                    'Line': line_num,
                    'Text': line
                }
                results.append(result)
    return results


from collections import Counter
def sort_results(results):
    """This function sorts a list of search results based on the file name in alphabetical order and returns it.

Arguments:
    results (list): A list of dictionaries containing search results, where each dictionary contains keys 'File', 'Line', and 'Text'.

Returns:
    list: A sorted list of dictionaries containing search results, where each dictionary contains keys 'File', 'Line', and 'Text'."""
    file_cnt = Counter(result['File'] for result in results)
    sorted_results = sorted(results, key=lambda x: file_cnt[x['File']], reverse=True)
    return sorted_results


def display_results(results):
    """This function takes a list of search results and displays them in a paginated format.
    Each page shows a maximum of 30 results. The function prompts the user to see more results if available.
    
    Args:
        results (list): A list of dictionaries representing the search results.

    Returns:
        None

    ."""
    if results:
        page_size = 30
        total_results = len(results)
        total_pages = (total_results - 1) // page_size + 1
        current_page = 1
        while True:
            print(f"Page {current_page} of {total_pages}")
            print()
            start_idx = (current_page - 1) * page_size
            end_idx = min(start_idx + page_size, total_results)
            for idx, result in enumerate(results[start_idx:end_idx], start=start_idx+1):
                print(f"result {idx}:")
                print(f"File: {result['File']}")
                print(f"Line: {result['Line']}")
                print(f"Text: {result['Text']}")
                print()
            if total_results > end_idx:
                show_more = input("Do you want to see more results?(Yes/No): ")
                print()
                if show_more.lower() == 'yes':
                    current_page += 1
                else:
                    break
            else:
                break
    else:
        print("Unfortunately, no results matching your search were found!")
        print()


def search_engine():
    while True :
        print("-----------------------")
        print("|search_engine_by_sara|")
        print("-----------------------")
        print()
        user_query = get_user_query()
        files_content = read_files()
        if ' ' in user_query:
            search_results = search_query_multi_words(user_query, files_content)
        else:
                    search_results = search_query(user_query, files_content)
        sorted_results = sort_results(search_results)
        display_results(sorted_results)
        more_search = input("Do you want to perform another search?(Yes/No): ")
        while more_search.lower() not in ['yes', 'no']:
            more_search = input("please enter YES or NO: ")
        if more_search.lower() == "no":
            print()
            print("bye bye")
            break
    

search_engine()