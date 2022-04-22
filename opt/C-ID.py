





def add_0(_id):
    _id = '0' * (6 - len(_id)) + _id
    return _id

def create_id(prefecture, city):
    prefecture_id = str(prefecture)
    prefecture_id = add_0(prefecture_id)

    city_id = str(city)
    city_id = add_0(city_id)

    id = prefecture_id + city_id

    return id

def allocate_id(city_list, id_dict):
    city_list.sort()
    city = 1
    prefecture = 1

    for i in range(len(city_list)):
        p = city_list[i][0]
        if prefecture != p:
            prefecture = p
            city = 1
        
        id = create_id(prefecture, city)
        id_dict[city_list[i][2]] = id
        city += 1
    
    return id_dict

def print_answer(id_dict, m):
    for i in range(m):
        print(id_dict[i])
    

def main():
    n, m = map(int, input().split())
    city_list = []
    id_dict = {}
    for i in range(m):
        p, y = map(int, input().split())
        city_list.append([p, y, i])

    id_list = allocate_id(city_list, id_dict)

    print_answer(id_dict, m)

if __name__ == '__main__':
    main()




    
