# SearchDiscogs
Creating a new way to make a research in Discogs.

# Concept
I have always been frustrated about Discogs missing an important feature to me : the ability to make a search on several records at the same time.

Here is the concrete problem : 

* I want to find a seller that offers the record _Miles Davis - Kind of Blue_ : __Possible__
* I want to find a seller that offers the record _Miles Davis - Kind of Blue_ but __also__ _Michael Jackson - Thriller_ : __Impossible__

This repository is here to create this possibility!

# Currently working

For now here is how it works : 

* First way : on discogs,  get your developer token* and get the references of the records your searching for. Then, launch _py main.py token ref1 ref2 ref3_ and you'll see the most common sellers as a result.
* Second way : on discogs, get your developer token. Then, launch _py get_wantlist.py token_, it will generate a CSV file with your wantlist. Now, by executing _py get_reference.py "Miles Davis Kind of Blue" "Michael Jackson Thriller"_ you will find out directly the references. Eventually, you will be able to run  _py main.py token ref1 ref2 ref3_.

After doing so, you will in your shell the sellers that you could deal with ! 

_**To get your developer token, go to the developer settings of your account on the Discogs website._
_**To get reference, go to a discogs page and look at the top right. You'll find something like r23456. Just keep the numbers! For example, [here](https://www.discogs.com/fr/Miles-Davis-Kind-Of-Blue/release/8359573) the ref is 8359573._
# To Do

There are still many things to do ! 
For now the main points are:  

    - Add a cli parameter __wantlist__ or __ref__ > make it possible to run main.py directly with record names
    - ? We'll find more !





