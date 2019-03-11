from stacks import Stack

def decimalTobinary(decimal):
    st = Stack()
    while decimal > 0:
        res = decimal % 2
        st.push(res)
        decimal = decimal // 2

    binary = ""
    while not st.is_empty():
        binary = binary + str(st.pop())

    return binary


print(decimalTobinary(7))