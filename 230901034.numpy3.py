{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "95d74a3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([1, 4]),)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([1,6,2,7,6,5])\n",
    "x=np.where(arr==6)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3ae2dccb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([1, 2, 4]),)\n"
     ]
    }
   ],
   "source": [
    "x=np.where(arr%2==0)\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d7664092",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([0, 3]),)\n"
     ]
    }
   ],
   "source": [
    "x=np.where(arr%3==1)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a950b05c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([0,1,2,2,7,8,9])\n",
    "x=np.searchsorted(arr,8,side='right')\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "baf1c9c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4 5 6 7 9]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr=np.array([9,5,2,7,6,4])\n",
    "print(np.sort(arr))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6d029ead",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[4 7 9]\n",
      " [1 4 9]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1=np.array([[7,4,9],[9,1,4]])\n",
    "print(np.sort(arr1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3f4e902a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 31  78 100]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr2=np.array([31,78,69,100])\n",
    "x=[True,True,False,True]\n",
    "newarr=arr2[x]\n",
    "print(newarr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "02f89030",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[False False False False False False]\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr3=np.array([31,78,69,100])\n",
    "filter_arr=arr>70\n",
    "newarr=arr>70\n",
    "newarr=arr[filter_arr]\n",
    "print(filter_arr)\n",
    "print(newarr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75ef0517",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
