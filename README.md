# HTML Corpus
To easily annotate our legal corpus I needed software capable of saving concurring sentences and names of judges forming the majority.
Since the research is conducted in Tokyo and annotators are in the UK, I build a simple web app to allow for a fast annotation of our corpus.

While the are tools such as [Brat](http://brat.nlplab.org/) available, they focus on annotation of words, not sentences and/or whole documents.
The code takes corpus in .txt and turns it into .html sites where every line is an item of a form. See [Annotator](https://github.com/valvoda/annotator) for details on the server using the HTML Corpus.

## Getting Started

To get html versions of your corpus for use in the [Annotator](https://github.com/valvoda/annotator), simply run htmlcorp.py

## Authors

* **Josef Valvoda**

## License

This project is licensed under the MIT License - [LICENSE.md](LICENSE)
