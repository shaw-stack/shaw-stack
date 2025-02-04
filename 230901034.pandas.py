{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83d128a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.DataFrame()\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc69ce43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "series to Dataframe \n",
      "\n",
      "      emp  ID\n",
      "0     uma  10\n",
      "1    siva  20\n",
      "2  sindhu  30\n",
      "3    ravi  40\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "emp=pd.Series([\"uma\",\"siva\",\"sindhu\",\"ravi\"])\n",
    "id=pd.Series([10,20,30,40])\n",
    "frame={'emp':emp,'ID':id}\n",
    "Result=pd.DataFrame(frame)\n",
    "print(\"series to Dataframe \\n\")\n",
    "print(Result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3f960664",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Extracting the Second row \n",
      "\n",
      "      emp  ID\n",
      "0     uma  10\n",
      "1    siva  20\n",
      "2  sindhu  30\n",
      "3    ravi  40\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Extracting the Second row \\n\")\n",
    "print(Result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "ad8d9b05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      emp  ID  Age\n",
      "0     uma  10   20\n",
      "1    siva  20   18\n",
      "2  sindhu  30   20\n",
      "3    ravi  40   50\n"
     ]
    }
   ],
   "source": [
    "Result['Age']=pd.Series([20,18,20,50])\n",
    "print(Result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "29241fe0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      emp  ID\n",
      "0     uma  10\n",
      "1    siva  20\n",
      "2  sindhu  30\n",
      "3    ravi  40\n"
     ]
    }
   ],
   "source": [
    "del Result ['Age']\n",
    "print(Result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6a1ba61c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Slice Row\n",
      "       emp  ID\n",
      "1    siva  20\n",
      "2  sindhu  30\n"
     ]
    }
   ],
   "source": [
    "print(\"Slice Row\\n\",Result[1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c886510f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Extracting the second row \n",
      "\n",
      "emp    siva\n",
      "ID       20\n",
      "Name: 1, dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n Extracting the second row \\n\")\n",
    "print(Result.loc[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39164d66",
   "metadata": {},
   "outputs": [],
   "source": [
    "()"
   ]
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
