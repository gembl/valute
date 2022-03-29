from PIL import Image
import numpy as np

E = 0
I = 0

def great():
    print("__________________________________________________________________")
    print("               Приветствуем Вас!")
    print("__________________________________________________________________")
    print("  Данная программа высчитывает количество фигур на картинке   ")
    print("               Выберите ее номер  ")


def show_images(choice_show):
        if choice_show == "1":
            name_image = 'test.jpg'
            im = Image.open(name_image)
            im.show(name_image)
            open_images(name_image)
        elif choice_show == '2':
            name_image = 'test1.jpg'
            im = Image.open(name_image)
            im.show()
            open_images(name_image)

def open_images(name_image):
    im = Image.open((name_image))
    im_1 = im.convert('1')
    im_array = np.array(im_1)
    im_plus = np.zeros((im.height + 2, im.width + 2))
    for L in range(im_plus.shape[0]):
        for P in range(im_plus.shape[1]):
            if L != 0 and P != 0 and L != 1 and P != 1 and (P != im_plus.shape[1]) and (L != im_plus.shape[0]) and \
                    (P != im_plus.shape[1]-1) and (L != im_plus.shape[0]-1):
                im_plus[L][P] = not im_array[L-2][P-2]
    count_objects(E, I, im_plus)

def external_match(L,P,E, im_plus):
    if im_plus[L][P] == False and im_plus[L+1][P] == False and im_plus[L][P+1] == False and im_plus[L+1][P+1] == True:
        E += 1
    elif im_plus[L][P] == False and im_plus[L+1][P] == False and im_plus[L][P+1] == True and im_plus[L+1][P+1] == False:
        E += 1
    elif im_plus[L][P] == False and im_plus[L+1][P] == True and im_plus[L][P+1] == False and im_plus[L+1][P+1] == False:
        E += 1
    elif im_plus[L][P] == True and im_plus[L+1][P] == False and im_plus[L][P+1] == False and im_plus[L+1][P+1] == False:
        E += 1
    return E

def internal_match(L,P,I, im_plus):
    if (im_plus[L][P] == False) and (im_plus[L+1][P] == True) and (im_plus[L][P+1] == True) and (im_plus[L+1][P+1] == True):
        I += 1
    elif (im_plus[L][P] == True) and (im_plus[L+1][P] == False) and (im_plus[L][P+1] == True) and (im_plus[L+1][P+1] == True):
        I += 1
    elif im_plus[L][P] == True and im_plus[L+1][P] == True and im_plus[L][P+1] == False and im_plus[L+1][P+1] == True:
        I += 1
    elif im_plus[L][P] == True and im_plus[L+1][P] == True and im_plus[L][P+1] == True and im_plus[L+1][P+1] == False:
        I += 1
    return I

def count_objects(E, I, im_plus):
    for L in range(im_plus.shape[0]-1):
        for P in range(im_plus.shape[1]-1):
            E = external_match(L, P, E, im_plus)
            I = internal_match(L, P, I, im_plus)
    figure = (E - I) / 4
    print("     E (количество внешних углов):", E)
    print("     I (количество внутренних углов):", I)
    print("     Количество фигур:", int(figure))


def main():
    great()
    print('Команды:',
          '\n1 - первое изображение',
          '\n2 - второе изображение',
         )
    choice_show = input("Введите номер изображения: ")
    show_images(choice_show)


if __name__ == "__main__":
    main()
