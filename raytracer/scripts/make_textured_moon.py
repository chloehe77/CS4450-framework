

scene = """{
   "scene": {"type": "moverotation",
              "rotation": {"x": 21, "z": %d},
              "movement": {"y": 250},
              "child": {
                "type": "union",
                "children": [
                   {"type": "sphere",
                    "radius": 135,
                    "material": {"type": "textured", "ka": 0.2, "kd": 0.4, "ks": 0.7, "alpha": 100, "reflectiveness": 0.1, "texture": "earth.jpg"}},
                   {"type": "sphere",
                    "radius": 20,
                    "center": {"x": -250, "y": -50, "z": 50},
                    "material": {"type": "textured", "ka": 0.2, "kd": 0.8, "ks": 0.3, "alpha": 5, "texture": "deathstar.png"}} 
                    ]
                }
            },
   "camera": {"x": 0, "y": -100, "z": 0},
   "view": {"x": 0, "y": 1, "z": 0},
   "background": {"r": 128, "g": 128, "b": 128},
   "reflections": 1,
   "lighting": {"type": "phong", "ambient": {"color": 128}, "shadows": true,
                "lights": [{"position": {"x": -50, "y": -700, "z": 30}, "color": {"r": 255, "g": 0, "b": 0}},
                           {"position": {"x": 50, "y": -700, "z": 30}, "color": {"r": 0, "g": 255, "b": 0}},
                           {"position": {"x": 0, "y": -700, "z": -60}, "color": {"r": 0, "g": 0, "b": 255}}]}
}"""


for i in range(100):
   f = open("scene%03d.json"%(i), "w")
   f.write(scene%(i))
   f.close()