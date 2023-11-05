def search(dictionary):
    lst_answer_URL = []

    # input search
    query = input("What are you looking for?")

    # searchstr to lst
    query_str = query.split()

    # for word in lst:
    for word in query_str:
        # if word in dic.keys():
        if word in dictionary.keys():
            lst_answer_URL.append(dictionary.get(word))
        
