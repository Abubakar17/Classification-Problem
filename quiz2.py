import random
import matplotlib.pyplot as plt
import math

#defining and plotting C [a rectangle from 1,2 to 3,4]
C_rect = plt.Rectangle((2, 1), 2, 2, linewidth=1, edgecolor='b', facecolor='none' ,label='C')
plt.gca().add_patch(C_rect)

#PREPARING TRAINING DATA: 
#coordinates are stored in a list i.e [(x1,y1), (x2,y2)...]

#positive training data generation
posi =[]
for i in range(8):              # 8 data points
    x = random.uniform(2,3.75)  # x should be between 2 and 3.75
    y = random.uniform(1,2.5)   # y between 1 and 2.5
    coordinate = [x,y]
    posi.append(coordinate)
plt.scatter([point[0] for point in posi], [point[1] for point in posi], marker='+', label='pos')

#negative training data generation
count =0
negs= []
while count<48:                 # generate 48 coordinates
    x = random.uniform(0,5)     # anywhere between 0 and 5
    y = random.uniform(0,5)
    if x>2 and x<4 and y>1 and y<3: #shouldnt coincide with positive data
        continue
    else:
        coordinate = [x,y]
        negs.append(coordinate)
        count+=1
plt.scatter([point[0] for point in negs], [point[1] for point in negs], marker='x', label='negs')

# PLOTTING S HYPOTHESIS
#finding the minimum and maximum of positive training data
s_min_x = min(x for x, _ in posi)
s_max_x = max(x for x, _ in posi)
s_min_y = min(y for _, y in posi)
s_max_y = max(y for _, y in posi)
rect_width = s_max_x - s_min_x
rect_height = s_max_y - s_min_y

S_rectangle = plt.Rectangle((s_min_x, s_min_y), rect_width, rect_height, linewidth=1, edgecolor='r', facecolor='none',label='S',linestyle='dotted')
plt.gca().add_patch(S_rectangle)


#PLOTTING G HYPOTHESIS
#initializing extreme values (to be replaced by actual points)
g_max_x = 5
g_min_y  =0
g_max_y =5
g_min_x= 0

#go through each negative example and find the nearest points to each side of the S hypothesis rectangle
for x,y in negs:
    if y>g_min_y  and y<(s_min_y+rect_height) and x>s_min_x and x<(s_min_x+rect_width):
        g_min_y = y #since we only require the minimum y value from this condition
    if y<g_max_y and y>(s_min_y+rect_height) and x>s_min_x and x<(s_min_x+rect_width):
        g_max_y = y #maximum y value
for x,y in negs:
    if x<s_min_x and x>g_min_x and y<g_max_y and y>g_min_y :
        g_min_x = x #getting minimum x value
    if x>(s_min_x + rect_width) and x<g_max_x and y<g_max_y and y>g_min_y :
        g_max_x = x #max x value

G_rectangle = plt.Rectangle((g_min_x, g_min_y ), g_max_x-g_min_x,  g_max_y-g_min_y , linewidth=1, edgecolor='black', facecolor='none', label='G',linestyle='dotted')
plt.gca().add_patch(G_rectangle)

#finally showing the figure TRAINING COMPLETE HYPOTHESIS GENERATED
#uncomment these lines to show training data and rectangles created
#plt.legend()
#plt.show()  


#TEST DATA 
#Using same variables since we dont really need the previous ones anymore

#positive test data generation [10 data points]
posi =[]
for i in range(10):
    x = random.uniform(2,4)     #this time the ranges are a bit different 
    y = random.uniform(1,3)     #the ranges are of C hypothesis and not the S hypothesis
    coordinate = [x,y]
    posi.append(coordinate)
plt.scatter([point[0] for point in posi], [point[1] for point in posi], marker='+', label='test pos')


#negative test data generation [50 data points]
count =0
negs= []
while count<50:             #generate 50 coordinates
    x = random.uniform(0,5) #temp anywhere between 0 and 5
    y = random.uniform(0,5)
    if x>2 and x<4 and y>1 and y<3: #shouldnt coincide with positives
        continue
    else:
        coordinate = [x,y]
        negs.append(coordinate)
        count+=1
plt.scatter([point[0] for point in negs], [point[1] for point in negs], marker='x', label='test negs')

#counting the number of positives in S and G respectively 
posi_s = 0
posi_g = 0
for x,y in posi:
    if x<=s_max_x and x>=s_min_x and y<=s_max_y and y>=s_min_y:
        posi_s +=1                  #counting positives inside S
    elif x<=g_max_x and x>=g_min_x and y<=g_max_y and y>=g_min_y:
        posi_g +=1                  #counting positives inside G
posi_g +=posi_s                     #all points enclosed in S are also counted as enclosed in G

#counting the number of negatives in S and G respectively 
neg_s = 0
neg_g = 0
for x,y in negs:
    if x<=s_max_x and x>=s_min_x and y<=s_max_y and y>=s_min_y:
        neg_s +=1                   #negs in S (this must logically be 0 always but it never hurts to count)
    elif x<=g_max_x and x>=g_min_x and y<=g_max_y and y>=g_min_y:
        neg_g +=1                   #negs in G
neg_g +=neg_s                       #all points enclosed in S are also counted as enclosed in G 

#instead of using the whole formula, I hv used a simplified form.
print("Percentage of positive points falling in S:", posi_s*10,"%") 
print("Percentage of negative points falling in S:", neg_s*2, "%")
print("Percentage of positive points falling in G:", posi_g*10, "%")
print("Percentage of negative points falling in G:", neg_g*2, "%")

#finally showing the figure
#TESTING DATA INCLUDED
plt.title("Scatter plot of Training + Test data")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()