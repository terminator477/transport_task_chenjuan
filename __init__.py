eg1 = {"neighbours" : {
            "A": ["B", "C","D"],
            "B": ["A","E"],
            "C": ["A"],
            "D": ["A"],
            "E": ["B"],
        },
    "attributes" : {
            "cost": {
                ("A", "B"): 101,
                ("A", "D"): 79,
                ("A", "C"): 37,
                ("E", "B"): 85,
                ("B", "A"): 101,
                ("B", "E"): 85,
                ("C", "A"): 37,
                ("D", "A"): 79,
            },

            "distance": {
                ("A", "B"): 1010,
                ("A", "D"): 790,
                ("A", "C"): 370,
                ("E", "B"): 850,
                ("B", "A"): 1010,
                ("B", "E"): 850,
                ("C", "A"): 370,
                ("D", "A"): 790,
            }
        },
        #流量和cost数值相等
        "lis" : [[0,101,37,79,186],
                 [101,0,138,180,85],
                 [37,138,0,116,223],
                 [79,180,116,0,265],
                 [186,85,233,265,0]]}