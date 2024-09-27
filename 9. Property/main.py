class Rect:

    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return(f"{self._width:.1f}cm")


    @property
    def height(self):
        return(f"{self._height}")


    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width=new_width
        else:
            print("Inlcude valid width")    

    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._width=new_height
        else:
            print("Inlcude valid height") 

re1=Rect(1,20)

re1.width=13
re1.height=22

print(re1._width)