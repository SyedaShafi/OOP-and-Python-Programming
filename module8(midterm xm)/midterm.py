import datetime

class Star_Cinema:
    __hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__cols = cols
        self.__rows = rows
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)
      
    
    def entry_show(self, id, movie_name, time):
        self.__twoD_List = []
        self.__oneD_List = []
        self.__list = (id, movie_name, time)
        self.__show_list.append(self.__list)
        for i in range(self.__rows+1):
            self.__oneD_List = [0] * self.__cols
            self.__twoD_List.append(self.__oneD_List)
        self.__seats[id] = self.__twoD_List


    def book_seat(self, id):
        if id in self.__seats:
            print("NUMBER OF TICKETS:?", end = "")
            n = int(input())
            i = 0
            while i < n:
                print("SELECT THE ROW AND COL FOR SEAT: ", end = "")
                r, c = map(int, input().split())
                if((r>=0 and r<len(self.__seats[id])) and (c>=0 and c<len(self.__seats[id])) ):
                    if (self.__seats[id][r][c] == 0):
                        self.__seats[id][r][c] = 1
                        print(f"SEAT BOOKED IN THE ROW: {r} AND COL: {c}.")
                        i+=1
                    else:
                        print("THE SEAT IS ALREADY BOOKED.")
                else:
                    print("THIS ROW AND COL IS OUT OF RANGE.")
                   
        else:
            print("THE SHOW WITH ID:{id} IS NOT AVAIABLE.")


    def view_show_list(self):
        print('------------------------------------------')
        for ele in self.__show_list:
            print(f"MOVIE NAME: {ele[1]}({ele[0]}) SHOW ID: {ele[0]} TIME: {ele[2]} ")
        print('------------------------------------------')

    def view_available_seats(self, id):
        if(id in self.__seats):
            for eles in self.__seats[id]:
                for ele in eles:
                    print(ele, end = " ")
                print()
        else:
            print("INVALID SHOW ID.")

now = datetime.datetime.now()
hall_obj = Hall(10, 10, 1)
hall_obj.entry_hall(101)
hall_obj.entry_show(801, 'XYZ',now)
hall_obj.entry_show(809, 'ABC',now)
inpt=1
while 1 :
    if (inpt >=4 or inpt<=0):
        break
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    print("ENTER OPTION:", end="")
    inpt = int(input())
    if(inpt == 1):
        hall_obj.view_show_list()
    elif(inpt == 2):
        print("ENTER SHOW ID: ", end = "")
        id = int(input())
        hall_obj.view_available_seats(id)
    elif(inpt == 3):
        print("ENTER SHOW ID: ", end = "")
        id = int(input())
        hall_obj.book_seat(id)
    else:
        break

