all: build/main.pdf

# hier alle zu erstellenden Plots
plots: build/plot_NAME.pdf

# für jeden zu erstellenden Plot:
build/plot_NAME.pdf: python/plot1.py data/*.csv | build
	python python/plot1.py

build/main.pdf: plots

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	latex/main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean plots
