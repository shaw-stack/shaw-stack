{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8a22b53f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20 40 50 70 10]\n",
      "[6 2 9 7 1]\n",
      "[26 42 59 77 11]\n",
      "[14 38 41 63  9]\n",
      "[120  80 450 490  10]\n",
      "[ 3.33333333 20.          5.55555556 10.         10.        ]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr1=[20,40,50,70,10]\n",
    "arr2=[6,2,9,7,1]\n",
    "a=np.array(arr1)\n",
    "b=np.array(arr2)\n",
    "print(a)\n",
    "print(b)\n",
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a*b)\n",
    "print(a/b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b8dcabf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1150\n",
      "sclr value: 3\n",
      "array: [20 40 50 70 10]\n",
      "result [ 60 120 150 210  30]\n"
     ]
    }
   ],
   "source": [
    "print(a.dot(b))\n",
    "sclr=3\n",
    "print(\"sclr value:\",sclr)\n",
    "print(\"array:\",a)\n",
    "print(\"result\",a*sclr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "671c4203",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 6]\n",
      " [0 4]]\n"
     ]
    }
   ],
   "source": [
    "a=np.array([[10,20],[30,40]])\n",
    "b=np.array([[3,7],[5,9]])\n",
    "print(a%b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0eb982f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "array1: [10, 7, 2]\n",
      " array2: [6, 5, 3]\n",
      "result: [4 2 5]\n"
     ]
    }
   ],
   "source": [
    "def my_fun(x,y):\n",
    "    if x>y:\n",
    "        return x-y\n",
    "    else:\n",
    "        return x+y\n",
    "arr1=[10,7,2]\n",
    "arr2=[6,5,3]\n",
    "vect_fun=np.vectorize(my_fun)\n",
    "print(\"array1:\",arr1)\n",
    "print(\" array2:\",arr2)\n",
    "print(\"result:\",vect_fun(arr1,arr2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "138c82d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (476313318.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[12], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    -\u001b[0m\n\u001b[0m     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "-"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90e615b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3074102",
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
