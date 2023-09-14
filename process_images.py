import cv2
import matplotlib.pyplot as plt


class DataExtractor:
    TEMPLATE_WIDTH = 944
    METHOD = cv2.TM_CCOEFF_NORMED

    def __init__(self, path_img: str, path_template: str):
        self.path= path_img
        self.path_template = path_template
        
        self.load_image()
        self.load_template()
        
        
    def load_image(self):
        img = cv2.imread(self.path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (0,0), fx=self.TEMPLATE_WIDTH/img.shape[1], fy=self.TEMPLATE_WIDTH/img.shape[1])
        self.img = img
        
    def load_template(self):
        template = cv2.imread(self.path_template)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        self.template = template
        
    def find_anchor_and_scale(self):
        val = 0
        loc = 0
        loc_b = 0
        t_scale = 0
        
        
        for scale in range(50,160):

            cur_template = self.template.copy()
            cur_template = cv2.resize(cur_template, (0,0), fx=scale/100, fy=scale/100)
            result = cv2.matchTemplate(self.img, cur_template, self.METHOD)
            h, w = cur_template.shape
            _, max_val, _ , max_loc = cv2.minMaxLoc(result)

 
            location = max_loc
            corr = max_val
            bottom_right = (location[0]+ w, location[1] + h)
            if corr > val:
                val = corr
                loc = location
                loc_b = bottom_right
                t_scale = scale
        self.scale = t_scale/100
        self.anchor_up = loc
        self.anchor_down = loc_b
        
    def show_img(self):
        show_img = self.img.copy()
        cv2.rectangle(show_img, self.anchor_up, self.anchor_down, 0.5)
        plt.imshow(show_img, cmap="gray")
        plt.show()
    
            
ex = DataExtractor('/Users/robinfeldmann/Projects/opencv_tutorials/images/PHOTO3.jpg', '/Users/robinfeldmann/Projects/opencv_tutorials/templates/lower_bar.jpg')
ex.find_anchor_and_scale()
ex.show_img()