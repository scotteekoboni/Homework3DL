# conv.py file
import time
startTime = time.time()
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torch.autograd import Variable
import numpy as np
import random
import cv2
#import nn

#what is "input" in the "forward" method
#am i just outputting 1 hidden layer at a time?
#4. Part A: "By running forward(input) the script will perform the forward propagation pass on the network previously built using sigmoid nonlinearities."

class NeuralNetwork(): 

    def __init__(self, arrayZ):
        #3,4,1: 
        #(self, size of the input layer, size of the hidden layers, size of the output layer)
        #super(NeuralNetwork, self).__init__()
        #need to init the "netwrok" and theta(layer) <--(weights)
        #(3,4) matrix for first hidden layer the i guess (4,1) for the next

        #arrayZ = arrayZ

        ThetaDic = {}
        keys = []
        weights = []
        


        numHidLayers = len(arrayZ) -2 # of hidden layers 
        for i in range(0, numHidLayers+1):
            keys.append(i)

        print("This is the keys list:", keys)

        #Populating the dictionary below!!

        for i in range(0, numHidLayers+1): #runs through the h1, h2, h3
            numElements = arrayZ[i] 
            mean = 0
            SD = 1/(np.sqrt(numElements))

        for k in range(0, numElements+1):
            for i in range(0, numHidLayers+1):
                q = np.random.normal(mean, SD, ((arrayZ[i]+1),(arrayZ[i+1]))) #<--- use numpy thing where i can specify a mean = 0 and a SD
                #print("this is q:", q)
                x = torch.Tensor(q)
                #print("this is x: ", x)
                weights.append(x)

            
        self.ThetaDic = dict(zip(keys, weights))


        print("this is ThetaDic: ",self.ThetaDic)

        

        



    def getLayer(self, layer): #takes "layer number" to indicate which layer

        return self.ThetaDic[layer] #should return a 2D tensor of weights ....for one layer at a time


    #the forward script will perform the forward propagation pass on the "network"  previously built using sigmoid nonlinearities.
    def forward(self, input): #feedforward pass single vector

        z = []
        print("this is O.G. input",input)



        def sigmoid(x, Derivative=False):
            if not Derivative:
                return 1 / (1 + np.exp (-x))
            else:
                out = sigmoid(x)
                return out * (1 - out)






        #numExamples = input.shape[0]
        #print("numExamples:", numExamples)
        numLayers = len(self.ThetaDic)
        #print("haha",numLayers)
        
        #input = torch.t(input)
        #biases = torch.ones(1,numExamples+1)
        #print(biases)
        #input = torch.t(input)


        


        for d in range(0, numLayers):
            #self.ThetaDic[d] = torch.t(self.ThetaDic[d])
            #input = torch.t(input)
            #input = torch.t(input)

        
        #layerInput = []
        

            if input.type() == "torch.DoubleTensor":

                numExamples = (torch.t(input)).shape[0]
                print("this is numExamples",numExamples)
                biases = torch.ones(1,numExamples)
                print(biases)

                biases = biases.type(torch.DoubleTensor)
                self.ThetaDic[d] = self.ThetaDic[d].type(torch.DoubleTensor)
                print("theta is notT: ", self.ThetaDic[d])

                x=torch.cat([biases, input],0) # X
                print("this is x",x)
                

                #print("theta is T: ", self.ThetaDic[d])
                
                ThetaDic = torch.t(self.ThetaDic[d])
                print("theta is T: ", ThetaDic)

                z = torch.mm(ThetaDic,x)
                print("here is z nignog: ",z)
                zSig = sigmoid(z)
                print("here is zSig: ", zSig)
                input = z



            else:
                print("kkkk",input)
                numExamples = (input).numpy()
                print("this is numExamplesssssssssssss s",numExamples)
                numExamples =  numExamples.size 
                print("this is numExamplesssssssssssss s",numExamples)
                biases = torch.ones(1,numExamples-1)
                print("BIASES",biases)
                print("input = ", input)

                # if input.shape == biases.shape:
                #     print("Looks good to me!")
                # else:
                #     input = torch.t(input)

                x = torch.cat([biases, input],0)
                print("this is x",x)
                ThetaDic = torch.t(self.ThetaDic[d])
                print("theta is T: ", ThetaDic)
                #x = [[x]
                z = torch.mm(ThetaDic,x)
                zSig = sigmoid(z)
                print("here is zSig: ", zSig)
                input = z

        return zSig




            #y = y.type(torch.Tensor)



            

        




        #     for index in range(numLayers):

        #         if index ==0:

        #             layerInput.append(torch.mm(self.ThetaDic[0],y))

        #         else:

        #             layerInput = torch.mm(torch.cat(self.ThetaDic[0], ([biases, self.layerOutput[-1]],0)))
        #     return self.layerOutput[-1].T

        # else:
        #     y=torch.cat([biases, input],0)

        #     for index in range(numLayers):

        #         if index ==0:
 
        #             layerInput = torch.dot(self.ThetaDic[0],y)

        #         else:

        #             layerInput = self.weights[index].dot(np.vstack(np.ones([1,numExamples],[self._layerOutput[-1]])))


        #     self._layerInput.append(layerInput)
        #     self._layerOutput.append(sigmoid(layerInput))

        # return self._layerOutput[-1].T



   # providing input , run it through the network, return result..?

    # so this needs to take a either a list (make it a tensor) or a tensor/matrix? and multiply it and the weights (specified theta) to get y. then get a z somehow
#matrix mult 
#add 1ones
#if input 1 D 
    #if (input == 1):






# # in the 2xn (2 cross n) and 1xn, "n" is the number of inputs into the gate--
# #AND gate will take n=2 inputs while the NOT gate will get just n=1 
# #so n number 

#         return output #? 1xn


#     def forward(self, input): #feedforward pass transposed design matrix



#     	return output #? 1xn




#     #if __name__ == "__main__":
#   	#main()


#     	class Shark:
#     def __init__(self, name):
#         self.name = name

#     def swim(self):
#         print(self.name + " is swimming.")

#     def be_awesome(self):
#         print(self.name + " is being awesome.")

# def main():
#     sammy = Shark("Sammy")
#     sammy.be_awesome()
#     stevie = Shark("Stevie")
#     stevie.swim()

# if __name__ == "__main__":
#   main()