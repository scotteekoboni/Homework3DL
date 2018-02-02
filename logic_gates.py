
from neural_network import NeuralNetwork
import torch

class AND():
    def __init__(self):
        self.nn = NeuralNetwork((2,1)) #IN , OUT
        numHidLayers = len((2,1)) -2

        for i in range(len(self.nn.ThetaDic)):
            theta = self.nn.getLayer(i)
            print("this is theta??: ", theta)


        for q in range(numHidLayers+1):
            rows = self.nn.ThetaDic[q].shape[0]
            columns = self.nn.ThetaDic[q].shape[1]

            for j in range(columns):
                for b in range(rows):
                    if b == 0:
                        self.nn.ThetaDic[j][b] = -5
                    else:
                        self.nn.ThetaDic[j][b] = 5

        print("the modified theta: ", self.nn.ThetaDic)

    def __call__(self, inp1, inp2): 
        return self.forward(inp1, inp2)

    def forward(self, inp1, inp2):
        # Convert boolean value to (0, 1)
        # tensor_inp <- inp1, inp2!!!!!!!! float or double tho

        if inp1 == True:
        	inp1 = True
        else:
        	inp1 = False
        if inp2 == True:
        	inp2 = True
        else:
        	inp2 = False

        inp1 = inp1 * 1
        inp2 = inp2 * 1
        print("this is inp1: ", inp1)
        print("this is inp2:  ", inp2)

        inputT1 = torch.Tensor(1,1)
        inputT1.add_(inp1)
        inputT2 = torch.Tensor(1,1)
        inputT2.add_(inp2)
        inputT = torch.cat([inputT1, inputT2], 0)

        # inputT = torch.DoubleTensor(inp1,inp2)

        print("here is inputTTTTTTT: ", inputT)
        #transInputT= torch.t(inputT)

        #y = forward(inputT)
        


        y = self.nn.forward(inputT)
        print("this is y sweetie: ", y)
        y= y.numpy()
        print("this is y sweetie: ", y)


        if y > 0.5:
            return True
        else:
            return False

        # if a == True :
        #     if b == True :
        #         return True
        #     else : 
        #         return False        






class OR():
    def __init__(self):
        self.nn = NeuralNetwork((2,1))
        theta = self.nn.getLayer(0)

        numHidLayers = len((2,1)) -2

        for i in range(len(self.nn.ThetaDic)):
            theta = self.nn.getLayer(i)
            print("this is theta??: ", theta)


        for q in range(numHidLayers+1):
            rows = self.nn.ThetaDic[q].shape[0]
            columns = self.nn.ThetaDic[q].shape[1]

            for j in range(columns):
                for b in range(rows):
                    if b == 0:
                        self.nn.ThetaDic[j][b] = -5
                    else:
                        self.nn.ThetaDic[j][b] = 5

        print("the modified theta: ", self.nn.ThetaDic)

    def __call__(self, inp1, inp2): 
        return self.forward(inp1, inp2)

    def forward(self, inp1, inp2):
        # Convert boolean value to (0, 1)
        # tensor_inp <- inp1, inp2!!!!!!!! float or double tho



        if inp1 == True:
            inp1 = True
        elif inp2 == True:
            inp2 = True
        else :
            inp1 = False
            inp2 = False




        #if inp1 == False:
        inp1 = inp1 * 1
        inp2 = inp2 * 1
        print("this is inp1: ", inp1)
        print("this is inp2:  ", inp2)

        inputT1 = torch.Tensor(1,1)
        inputT1.add_(inp1)
        inputT2 = torch.Tensor(1,1)
        inputT2.add_(inp2)
        print("inputT111111", inputT1)
        inputT = torch.cat([inputT1, inputT2], 0)

        print("here is inputTTTTTTTT: ", inputT)
        #transInputT= torch.t(inputT)

        #y = forward(inputT)
        


        y = self.nn.forward(inputT)
        print("this is y sweetie: ", y)
        y= y.numpy()
        print("this is y sweetie: ", y)
        if y >= 0.5:
            return True
        else:
            return False





class NOT():
    def __init__(self):
        self.nn = NeuralNetwork((1,1))
        theta = self.nn.getLayer(0)

        numHidLayers = len((2,1)) -2

        for i in range(len(self.nn.ThetaDic)):
            theta = self.nn.getLayer(i)
            print("this is theta??: ", theta)

                # def AND(a,b):
                #     if a == True :
                #         if b == True :
                #             return True
                #     else : 
                #         return False

            for q in range(numHidLayers+1):
                rows = self.nn.ThetaDic[q].shape[0]
                columns = self.nn.ThetaDic[q].shape[1]

                for j in range(columns):
                    for b in range(rows):
                        if b == 0:
                            self.nn.ThetaDic[j][b] = -6
                        else:
                            self.nn.ThetaDic[j][b] = 5

            print("the modified theta: ", self.nn.ThetaDic)

    def __call__(self, inp1): 
        return self.forward(inp1)

    def forward(self, inp1):
        # Convert boolean value to (0, 1)
        # tensor_inp <- inp1, inp2!!!!!!!! float or double tho

        if inp1 == 1:
            inp1 = False
        else:
            inp1 = True

        inp1 = inp1 * 1
        #inp2 = inp2 * 1
        print("this is inp1: ", inp1)
        #print("this is inp2:  ", inp2)

        inputT = torch.Tensor(1,1)
        inputT.add_(inp1)

        #inputT = torch.cat([inputT1, inputT2], 0)

        print("here is inputT: ", inputT)
        #transInputT= torch.t(inputT)

        #y = forward(inputT)
        

        y = self.nn.forward(inputT)
        print("this is y sweetie: ", y)
        y= y.numpy()
        print("this is y sweetie: ", y)
        if y > 0.1:
            return True
        else:
            return False






class XOR():
    def __init__(self):
        self.nn = NeuralNetwork((2,2,1))
        theta = self.nn.getLayer(0)

        numHidLayers = len((2,1)) -2

        for i in range(len(self.nn.ThetaDic)):
            theta = self.nn.getLayer(i)
            print("this is theta??: ", theta)


            for q in range(numHidLayers+1):
                rows = self.nn.ThetaDic[q].shape[0]
                columns = self.nn.ThetaDic[q].shape[1]

                for j in range(columns):
                    for b in range(rows):
                        if b == 0:
                            self.nn.ThetaDic[j][b] = -5
                        else:
                            self.nn.ThetaDic[j][b] = 5

            print("the modified theta: ", self.nn.ThetaDic)

    def __call__(self, inp1, inp2): 
        return self.forward(inp1, inp2)

    def forward(self, inp1, inp2):
        # Convert boolean value to (0, 1)
        # tensor_inp <- inp1, inp2!!!!!!!! float or double tho


        
        if inp1 != inp2:
            inp1 = True
            inp2 = True
        else:
            inp2 = False
            inp1 = False

        inp1 = inp1 * 1
        inp2 = inp2 * 1
        print("this is inp1: ", inp1)
        print("this is inp2:  ", inp2)

        inputT1 = torch.Tensor(1,1)
        inputT1.add_(inp1)
        inputT2 = torch.Tensor(1,1)
        inputT2.add_(inp2)
        inputT = torch.cat([inputT1, inputT2], 0)

        print("here is inputT: ", inputT)
        #transInputT= torch.t(inputT)

        #y = forward(inputT)
        

        y = self.nn.forward(inputT)
        print("this is y sweetie: ", y)
        y= y.numpy()
        print("this is y sweetie: ", y)
        if y > 0.5:
            return True
        else:
            return False



