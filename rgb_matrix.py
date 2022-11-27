board_rgb_matrix = [[[97, 43, 15], [107, 39, 16], [117, 34, 20], [130, 31, 25], [148, 30, 30],[158, 27, 32],[175, 30, 35],[198, 33, 39], [222, 31, 38], [237, 28, 35], [238, 29, 34], [239, 28, 37],
                     [236, 27, 46], [240, 24, 60], [236, 24, 72], [232, 25, 85], [229, 20, 101], [226, 16, 117], [215, 15, 131], [214, 18, 143], [199, 39, 145], [186, 46, 145], [179, 50, 148],
                     [170, 52, 150], [159, 56, 146], [147, 56, 149], [141, 60, 153], [131, 61, 150], [124, 62, 155], [114, 65, 156]],
                    [[135, 76, 28], [148, 68, 35], [155, 63, 33], [175, 62, 39], [183, 55, 42], [183, 56, 42], [213, 40, 40], [227, 32, 37], [235, 35, 35], [236, 39, 47], [235, 42, 52],
                     [237, 38, 59], [231, 36, 64], [237, 32, 77], [238, 27, 95], [235, 23, 110], [229, 20, 122], [231, 13, 140], [221, 43, 144], [204, 56, 148], [195, 60, 153], [180, 62, 148],
                     [174, 58, 149], [159, 61, 154], [154, 59, 154], [139, 63, 147], [128, 63, 153], [122, 63, 151], [113, 62, 150], [103, 59, 151]],
                    [[166, 95, 48], [172, 92, 38], [184, 91, 43], [195, 76, 42], [204, 73, 38], [212, 64, 42], [225, 57, 36], [233, 48, 37], [238, 54, 44], [230, 64, 68], [237, 63, 78],
                     [240, 58, 80], [238, 58, 93], [235, 51, 105], [235, 50, 117], [241, 41, 137], [235, 49, 151], [219, 67, 153], [202, 73, 153], [187, 75, 160], [181, 71, 157],
                     [165, 72, 155], [157, 69, 155], [151, 64, 159], [136, 68, 150], [134, 61, 152], [120, 61, 151], [116, 60, 153], [102, 55, 160], [89, 49, 145]],
                    [[201, 130, 40], [214, 130, 42], [221, 118, 39], [233, 104, 39], [231, 105, 37], [234, 94, 35], [241, 96, 43], [239, 85, 51], [240, 79, 61], [235, 85, 83], [241, 93, 100],
                     [240, 88, 111], [237, 84, 111], [238, 84, 126], [240, 79, 138], [234, 82, 157], [223, 85, 160], [208, 86, 159], [191, 94, 164], [180, 90, 162], [170, 85, 162], [155, 78, 158],
                     [150, 75, 158], [143, 71, 160], [132, 66, 155], [123, 65, 152], [111, 62, 151], [102, 55, 151], [87, 52, 147], [72, 45, 141]],
                    [[231, 154, 38], [241, 152, 32], [247, 146, 28], [246, 140, 30], [247, 134, 37], [246, 119, 48], [244, 119, 61], [243, 110, 69], [242, 112, 82], [241, 118, 104],
                     [240, 117, 119], [239, 119, 129], [238, 119, 137], [237, 111, 148], [236, 103, 165], [230, 111, 173], [211, 113, 172], [199, 113, 176], [186, 113, 173], [172, 102, 171],
                     [157, 95, 166], [147, 89, 165], [142, 83, 163], [142, 83, 163], [121, 73, 158], [111, 69, 155], [98, 62, 152], [88, 51, 148], [73, 46, 145], [73, 46, 145]],
                    [[254, 180, 21], [252, 177, 32], [249, 171, 44], [251, 171, 58], [251, 167, 64], [246, 164, 78], [246, 151, 84], [245, 142, 97], [244, 136, 100], [245, 136, 114],
                     [243, 143, 134], [243, 143, 143], [243, 143, 153], [244, 140, 163], [242, 134, 184], [226, 140, 187], [209, 139, 189], [198, 140, 189], [187, 130, 182], [172, 121, 182],
                     [156, 115, 180], [156, 116, 179], [143, 104, 171], [134, 93, 167], [116, 80, 162], [99, 73, 160], [90, 66, 153], [76, 51, 145], [58, 47, 144], [44, 41, 123]],
                    [[255, 191, 19], [251, 193, 39], [249, 185, 43], [249, 183, 54], [255, 183, 92], [248, 173, 82], [251, 170, 101], [249, 162, 108], [246, 163, 120], [247, 160, 133],
                     [242, 159, 152], [247, 156, 154], [246, 157, 167], [244, 156, 172], [241, 158, 197], [222, 166, 202], [209, 166, 203], [205, 173, 209], [185, 151, 201], [167, 140, 193],
                     [154, 131, 187], [138, 118, 179], [128, 110, 177], [114, 101, 170], [103, 93, 164], [89, 84, 167], [78, 75, 162], [68, 65, 156], [50, 53, 150], [44, 47, 135]],
                    [[251, 209, 22], [252, 205, 46], [253, 200, 49], [255, 198, 65], [252, 199, 79], [250, 194, 84], [252, 186, 98], [250, 186, 106], [253, 178, 121], [251, 175, 133],
                     [248, 175, 143], [250, 178, 158], [244, 183, 175], [244, 181, 181], [238, 180, 200], [215, 183, 213], [204, 184, 218], [205, 188, 221], [179, 170, 208], [167, 159, 207],
                     [152, 148, 198], [131, 136, 193], [119, 124, 188], [106, 117, 179], [94, 106, 173], [81, 98, 171], [72, 90, 166], [62, 78, 162], [48, 68, 158], [38, 56, 154]],
                    [[253, 224, 24], [251, 221, 39], [252, 217, 51], [252, 216, 66], [251, 222, 76], [255, 216, 89], [253, 219, 96], [251, 214, 107], [246, 219, 123], [239, 225, 146],
                     [237, 221, 155], [232, 225, 179], [225, 224, 194], [220, 225, 203], [211, 223, 211], [198, 221, 227], [193, 217, 241], [192, 216, 240], [163, 202, 232], [152, 185, 225],
                     [137, 171, 217], [122, 162, 214], [112, 147, 203], [103, 132, 197], [87, 120, 187], [76, 108, 181], [66, 98, 173], [59, 91, 167], [50, 80, 159], [39, 69, 158]],
                    [[248, 236, 36], [248, 235, 43], [250, 235, 54], [249, 238, 70], [249, 240, 77], [249, 242, 93], [248, 240, 107], [239, 238, 130], [231, 235, 140], [222, 233, 156],
                     [216, 231, 172], [211, 232, 191], [209, 232, 203], [205, 233, 211], [199, 230, 214], [187, 229, 228], [177, 227, 242], [178, 226, 246], [160, 218, 245], [138, 213, 245],
                     [124, 198, 235], [113, 181, 228], [101, 168, 219], [92, 151, 209], [81, 139, 202], [76, 125, 192], [63, 110, 182], [56, 101, 176], [53, 91, 170], [46, 81, 165]],
                    [[246, 240, 59], [246, 238, 66], [245, 237, 70], [244, 239, 75], [241, 237, 87], [237, 238, 98], [230, 232, 122], [223, 230, 134], [216, 227, 134], [199, 224, 143],
                     [189, 222, 149], [183, 218, 162], [181, 218, 176], [176, 217, 183], [175, 219, 194], [172, 222, 215], [171, 221, 222], [167, 221, 229], [156, 215, 229], [135, 216, 236],
                     [115, 209, 246], [100, 203, 244], [97, 187, 233], [90, 170, 223], [85, 156, 210], [72, 137, 204], [64, 125, 192], [61, 111, 183], [57, 99, 175], [50, 92, 174]],
                    [[241, 236, 32], [242, 234, 45], [245, 238, 72], [244, 239, 78], [242, 236, 88], [236, 236, 104], [230, 232, 122], [223, 230, 134], [176, 214, 111], [169, 211, 117],
                     [160, 208, 125], [153, 207, 137], [146, 206, 152], [140, 205, 156], [142, 207, 167], [140, 208, 177], [140, 210, 192], [139, 209, 199], [131, 207, 204], [120, 206, 210],
                     [104, 203, 216], [87, 201, 225], [59, 198, 239], [55, 186, 237], [62, 169, 221], [59, 154, 211], [62, 137, 199], [57, 120, 189], [60, 110, 184], [52, 101, 179]],
                    [[224, 227, 32], [220, 224, 41], [214, 225, 45], [207, 223, 55], [200, 220, 64], [186, 213, 70], [174, 210, 76], [159, 204, 84], [144, 201, 89], [133, 198, 96],
                     [120, 195, 105], [115, 195, 113], [112, 193, 122], [108, 194, 131], [112, 194, 137], [112, 195, 149], [112, 197, 156], [115, 199, 166], [117, 200, 172], [109, 197, 180],
                     [97, 198, 186], [86, 196, 197], [67, 197, 205], [46, 195, 217], [29, 185, 225], [35, 168, 226], [38, 157, 215], [56, 140, 204], [48, 128, 189], [42, 115, 185]],
                    [[194, 216, 44], [189, 214, 48], [181, 211, 51], [171, 207, 57], [160, 204, 55], [149, 200, 60], [129, 194, 64], [121, 193, 67], [109, 188, 69], [94, 181, 68],
                     [84, 179, 75], [77, 178, 84], [70, 184, 89], [75, 183, 105], [81, 187, 115], [89, 188, 123], [89, 189, 125], [92, 191, 136], [97, 191, 139], [96, 192, 146],
                     [91, 192, 158], [80, 194, 171], [70, 192, 178], [53, 192, 195], [41, 191, 206], [22, 185, 218], [14, 174, 222], [22, 175, 210], [35, 149, 209], [39, 132, 201]],
                    [[158, 197, 56], [154, 196, 60], [148, 194, 61], [135, 190, 63], [126, 187, 68], [108, 180, 65], [99, 177, 68], [83, 169, 70], [81, 166, 71], [65, 158, 71],
                     [53, 157, 73], [45, 164, 72], [44, 169, 75], [43, 177, 76], [50, 180, 85], [57, 181, 93], [66, 184, 99], [73, 181, 112], [74, 186, 114], [84, 187, 118],
                     [82, 189, 133], [73, 189, 142], [69, 190, 159], [57, 190, 169], [46, 189, 184], [40, 191, 200], [25, 190, 210], [15, 178, 211], [14, 168, 218], [23, 159, 219]],
                    [[121, 165, 68], [118, 170, 62], [111, 167, 68], [101, 162, 67], [90, 164, 70], [76, 159, 71], [67, 151, 72], [56, 151, 69], [41, 145, 67], [32, 136, 67],
                     [25, 139, 67], [20, 145, 69], [21, 154, 73], [24, 161, 73], [28, 170, 76], [30, 178, 76], [44, 179, 77], [51, 180, 86], [57, 183, 93], [71, 180, 104],
                     [68, 184, 111], [57, 185, 124], [48, 187, 138], [42, 186, 148], [34, 186, 163], [29, 185, 172], [28, 186, 189], [21, 187, 200], [18, 182, 216], [15, 177, 225]]]

# O(n*m) where n*m are dimentionsof color matrix
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for i, element in enumerate(_2d_list):
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for j, item in enumerate(element):
                flat_list.append([tuple(item), (i, j)])
        else:
            flat_list.append(element)
    return flat_list

flattened_board_rgb_matrix = flatten_list(board_rgb_matrix)

#sorting the matrix based on all 3 RGBs
flattened_board_rgb_matrix = sorted(flattened_board_rgb_matrix, key=lambda x: x[0])
#print(flattened_board_rgb_matrix)
