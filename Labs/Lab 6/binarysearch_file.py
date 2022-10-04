def binary_search(the_list, the_key):
    low = 0
    high = len(the_list)-1
    while high - low >= 0:
        mid_index = (high + low) // 2
        mid_element = the_list[mid_index]
        # print("Low:", low, "High:", high, "Mid I:", mid_index, "Mid E:", mid_element)
        if mid_element == the_key:
            return mid_element
        elif the_key < mid_element:
            high = mid_index-1
        elif mid_element < the_key:
            low = mid_index+1
    return None


def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()


main()
