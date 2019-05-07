print("-=-" * 20)
print("Vamos desenhar retângulos!!!")
print("-=-" * 20)


def draw(width, height):
    x = "#" * width
    for i in range(1, height + 1):
        print(x)
    
    
width = int(input("digite a largura: "))
height = int(input("digite a altura: "))

draw(width, height)
