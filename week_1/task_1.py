{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using matplotlib backend: MacOSX\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import operator\n",
    "\n",
    "%matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "Location ='_ea07570741a3ec966e284208f588e50e_titanic.csv'\n",
    "df = pd.read_csv(Location)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "577 314\n"
     ]
    }
   ],
   "source": [
    "df\n",
    "# total_rows = df['Sex'].count\n",
    "total_rows = df['Sex'].value_counts()\n",
    "print(total_rows['male'],total_rows['female'] )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "891 549\n",
      "0.3838383838383838\n",
      "0.24\n",
      "28.0 29.7\n",
      "0.41\n",
      "Elizabeth\n"
     ]
    }
   ],
   "source": [
    "total = df['Survived'].count()\n",
    "survived = df[df['Survived'] == 0]['Survived'].count()\n",
    "print(total, survived)\n",
    "\n",
    "df.groupby(('Survived'))\n",
    "total_survived = df.groupby(('Survived')).size() / total \n",
    "print(total_survived[1])\n",
    "\n",
    "classs_count = df.groupby(('Pclass')).size()/ len(df)\n",
    "print(round(classs_count[1],2))\n",
    "df\n",
    "median_age =  df['Age'].median()\n",
    "mean_age =  df['Age'].mean()\n",
    "print(round(median_age,2),round(mean_age,2))\n",
    "pearson_corr =  df['SibSp'].corr(df['Parch'])\n",
    "print(round(pearson_corr,2))\n",
    "names = df[df['Sex'] == 'female']['Name'].mode()\n",
    "dict_popular = {}\n",
    "for n in names:\n",
    "    if \"(\" in n:\n",
    "        whole_name = n[n.find(\"(\")+1:n.find(\")\")]\n",
    "        n_splitted =  whole_name.split(\" \")\n",
    "        for splt in n_splitted:\n",
    "            if splt in dict_popular:\n",
    "                dict_popular[splt] += 1\n",
    "            else:\n",
    "                dict_popular[splt] = 1\n",
    "        \n",
    "    if 'Miss.' in n:\n",
    "        whole_name = n[n.find(\"Miss.\")+6:len(n)]\n",
    "        for splt in n_splitted:\n",
    "            if splt in dict_popular:\n",
    "                dict_popular[splt] += 1\n",
    "            else:\n",
    "                dict_popular[splt] = 1\n",
    "                \n",
    "sorted_dict = sorted(dict_popular.items(), key=operator.itemgetter(1))\n",
    "print(sorted_dict[len(sorted_dict)-1][0])\n",
    "\n",
    "               \n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
