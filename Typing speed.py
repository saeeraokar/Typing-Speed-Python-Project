{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "00b5a695-50a0-48d8-803e-b77c10c3e5e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from time import * \n",
    "import random as r\n",
    "def mistake(partest,usertest):\n",
    "    error = 0\n",
    "    for i in range(len(partest)):\n",
    "        try:\n",
    "            if partest[i]!= usertest[i]:\n",
    "                error = error + 1\n",
    "        except:\n",
    "            error = error + 1\n",
    "    return error \n",
    "\n",
    "def speed_time(time_s,time_e,userinput):\n",
    "    time_delay = time_e - time_s\n",
    "    time_R = round(time_delay,2)\n",
    "    speed = len(userinput)/time_R\n",
    "    return round(speed)\n",
    "    \n",
    "            \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0e3e946-428e-488b-8db0-c14e7c4e619e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ready to test : yes/no :  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    *****Typing Speed Calculator *****\n",
      "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Enter :  A paragraph is a self-contained unit of discourse in writing dealing with a particyular piint or idewa\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Speed :  3 w/sec\n",
      "Error :  18\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ready to test : yes/no :  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    *****Typing Speed Calculator *****\n",
      "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    ck = input(\"Ready to test : yes/no : \")\n",
    "    if ck == \"yes\" :\n",
    "        test = [\"A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.\"]\n",
    "        [\"My name is saee raokar\",\"Welcome to Typing Speed Test\"]\n",
    "        test1 = r.choice(test)\n",
    "        print(\"    *****Typing Speed Calculator *****\")\n",
    "        print(test1)\n",
    "        print()\n",
    "        print()\n",
    "        time_1 = time()\n",
    "        testinput = input(\" Enter : \")\n",
    "        time_2 = time()\n",
    "\n",
    "        print(\"Speed : \",speed_time(time_1,time_2,testinput),\"w/sec\")\n",
    "        print(\"Error : \",mistake(test1,testinput))\n",
    "    elif ck == \"no\" :\n",
    "        print(\"Thank you\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Wrong Input\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7598ec10-674e-48a0-afe3-d45a91b023e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ready to test? yes/no :  Yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "***** Typing Speed Calculator *****\n",
      "\n",
      "Welcome to Typing Speed Test\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter here :  Welcome to typing speeed test\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Results:\n",
      "Speed : 27 WPM\n",
      "Errors : 8\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from time import *\n",
    "import random as r\n",
    "\n",
    "def mistake(partest, usertest):\n",
    "    error = 0\n",
    "    for i in range(len(partest)):\n",
    "        try:\n",
    "            if partest[i] != usertest[i]:\n",
    "                error += 1\n",
    "        except:\n",
    "            error += 1\n",
    "    return error\n",
    "\n",
    "def speed_time(time_s, time_e, userinput):\n",
    "    time_delay = time_e - time_s\n",
    "    if time_delay == 0:\n",
    "        return 0\n",
    "    time_R = round(time_delay, 2)\n",
    "    \n",
    "    # characters per second\n",
    "    cps = len(userinput) / time_R\n",
    "    \n",
    "    # words per minute (optional common metric)\n",
    "    wpm = cps * 60 / 5\n",
    "    return round(wpm)\n",
    "\n",
    "while True:\n",
    "    ck = input(\"Ready to test? yes/no : \").lower()\n",
    "    \n",
    "    if ck == \"yes\":\n",
    "        test = [\n",
    "            \"A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.\",\n",
    "            \"My name is Saee Raokar\",\n",
    "            \"Welcome to Typing Speed Test\"\n",
    "        ]\n",
    "\n",
    "        test1 = r.choice(test)\n",
    "\n",
    "        print(\"\\n***** Typing Speed Calculator *****\\n\")\n",
    "        print(test1)\n",
    "        print()\n",
    "\n",
    "        time_1 = time()\n",
    "        testinput = input(\"Enter here : \")\n",
    "        time_2 = time()\n",
    "\n",
    "        print(\"\\nResults:\")\n",
    "        print(\"Speed :\", speed_time(time_1, time_2, testinput), \"WPM\")\n",
    "        print(\"Errors :\", mistake(test1, testinput))\n",
    "        print()\n",
    "\n",
    "    elif ck == \"no\":\n",
    "        print(\"Thank you for using the Typing Tester!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Wrong input, type yes or no\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97ba557c-86b6-44db-8f4b-35a6bf186177",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e51abbb0-2021-4bc5-bd93-7187ef08804c",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
