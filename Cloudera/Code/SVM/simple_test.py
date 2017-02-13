from sklearn import svm
#Values <=2 classified as 0. Values >2 classified as 1.
print("The intent is for the machine to learn to classify coordinates <=[2,2] as 0, and coordinates >[2,2] as 1.")
X=[[0,0], [1,1], [2,2], [3,3], [4,4], [5,5]]
y=[0,0,0,1,1,1]
machine=svm.SVC()
machine.fit(X,y)

print("[-1,-1] classified as: "+str(machine.predict([[-1.,-1.]])))
print("[1,2] classified as: "+str(machine.predict([[1,2]])))
print("[2.4,2.4] classified as "+str(machine.predict([[2.4,2.4]])))
print("[2.5,2.5] classified as "+str(machine.predict([[2.5,2.5]])))
print("[2.6,2.6] classified as "+str(machine.predict([[2.6,2.6]])))
print("[6,6] classified as: "+str(machine.predict([[6,6]])))
