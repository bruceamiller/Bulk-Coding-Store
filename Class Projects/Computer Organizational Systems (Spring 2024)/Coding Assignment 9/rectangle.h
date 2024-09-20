#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
    public:
        Rectangle(int a = 0, int b = 0);
        Rectangle(const Rectangle &obj);
        ~Rectangle();
        int area();

    private:
        int width;
        int height;
};

#endif