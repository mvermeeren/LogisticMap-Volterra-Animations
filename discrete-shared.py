from manim import *

#rabbit.png and fox.png edited versions of:
#https://freesvg.org/1384316344
#https://commons.wikimedia.org/wiki/File:Foxx.svg


class Volterra(Scene):
    def construct(self):
        h=.1
        pts = [[5,7]]
        y,x = pts[-1]

        axes = Axes(
                    x_range=[0, 5, 5],
                    y_range=[0, 30, 30],
                    x_length=10,
                )
        labels = axes.get_axis_labels(x_label="\\text{time}", y_label="\\text{population}")
        self.add(axes,labels)
    
        fox = ImageMobject("fox.png").scale(x/40).move_to(Dot(axes.coords_to_point(2.5,28)))
        rabbit = ImageMobject("gray_rabbit.png").scale(y/40).move_to(axes.coords_to_point(4,28))

        self.add(fox)
        self.add(rabbit)

        self.add( Dot(axes.coords_to_point(0,x/5)).set_color(ORANGE) )
        self.add( Dot(axes.coords_to_point(0,y)).set_color(WHITE) )
        for i in range(50):
            y,x = pts[-1]
            xnew = .5*x*(1+h*y)
            ynew = 2*y/(1+h*xnew)
            pts += [[ynew,xnew]]
            self.wait(max(9/(i+3),1))
            self.add(Dot(axes.coords_to_point(.1*(i+1),xnew/5)).set_color(ORANGE))
            self.add(Dot(axes.coords_to_point(.1*(i+1),ynew)).set_color(WHITE))
            fox.scale(xnew/x) 
            rabbit.scale(ynew/y) 
            self.add( Line(axes.coords_to_point(.1*i,x/5),axes.coords_to_point(.1*(i+1),xnew/5)).set_color(ORANGE) )
            self.add( Line(axes.coords_to_point(.1*i,y),axes.coords_to_point(.1*(i+1),ynew)).set_color(WHITE) )
        self.wait(5)



class Logistic(Scene):
    def construct(self):
        h=.1
        pts = [.7]
        y = pts[-1]

        axes = Axes(
                    x_range=[0, 5, 5],
                    y_range=[0, 1.2, 1.2],
                    x_length=10,
                )
        labels = axes.get_axis_labels(x_label="\\text{time}", y_label="\\text{population}")
        self.add(axes,labels)
    
        cage = ImageMobject("meadow.png").scale(.5).move_to(axes.coords_to_point(2.5,1.1))
        rabbit = ImageMobject("gray_rabbit.png").scale(.5*y).move_to(axes.coords_to_point(2.5,1.1))

        self.add(cage,rabbit)

        self.add(Dot(axes.coords_to_point(0,pts[-1])))
        for i in range(50):
            y = pts[-1]
            ynew = 3.8*y*(1-y)
            pts += [ynew]
            self.wait(max(9/(i+3),1))
            self.add(Dot(axes.coords_to_point(.1*(i+1),pts[-1])))
            rabbit.scale(ynew/y) 
            self.add(Line(axes.coords_to_point(.1*i,pts[-2]),axes.coords_to_point(.1*(i+1),pts[-1])).set_opacity(.2))
        self.wait(5)
