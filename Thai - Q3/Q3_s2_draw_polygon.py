# Step 2: Draw a polygon
'''
Vẽ đa giác đều từ việc ghép nối các đoạn thẳng đã vẽ từ bước 1
Các tham số của hàm:
   - t: turtle object (đối tượng bút vẽ)
   - sides: số cạnh của đa giác ban đầu (>= 3)
   - side_length: độ dài mỗi cạnh ban đầu (pixels)
   - depth: độ sâu đệ quy (>= 0) (số lần áp dụng quy tắc)
   - inward = True: tam giác lõm vào trong (indentation inward)
'''

from Q3_s1_draw_line import line

def polygon(t, sides, side_length, depth, inward = True):
    '''
    1. Xác định góc quay ngoài (external turn - clockwise) để di chuyển
       từ cạnh này sang cạnh khác.
    2. Định hướng vẽ đa giác:
       - Dùng hàm lặp for để vẽ đủ số cạnh của polygon, với từng đoạn được
         lấy thông số từ code vẽ line
       - Đi vòng polygon theo chiều phải (chiều kim đồng hồ) 
    '''
    turn_angle = 360.0 / sides
    for _ in range(sides):
        line(t, side_length, depth)
        t.right(turn_angle) 