import pygame



class Entity(pygame.sprite.Sprite):
    def __init__(self,name):
        self.name = name
        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1
        self.angle = 0
        self.components = {}
        self.updatable_components = []
        self.renderable_components = []
        
        
    def start(self):
        
        print("Starting entity: " + self.name)
        
    
    def update(self,dt):
        for component in self.updatable_components:
            component.update(dt)
            
    def render(self,screen):    
        for component in self.renderable_components:
            component.render(screen)
            
    def destroy(self):
        print("Destroying entity: " + self.name)
        
        
        
        
    def set_position(self,x,y):
        self.x = x
        self.y = y
    
    def set_size(self,width,height):    
        self.width = width
        self.height = height
    
    def set_rotation(self,angle):
        self.angle = angle
        
    
    
    def translate(self,x,y):
        self.x += x
        self.y += y
    
    def scale(self,width,height):
        self.width *= width
        self.height *= height
            
    def rotate(self,angle):
        self.angle += angle
        
        
    
    def get_position(self):
        return (self.x,self.y)
    
    def get_size(self):
        return (self.width,self.height)
    
    def get_rotation(self):
        return self.angle
        
        
        
    def add_component(self,component):
        "component = component_class(self)"
        self.components[component.name] = component
        
        if hasattr(component,"update"):
            self.updatable_components.append(component)
        if hasattr(component,"render"):
            self.renderable_components.append(component)
            
        return component
    
    "def get_component(self, component_class):"
    "return self.components.get(component_class, None)"
