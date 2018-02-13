# IF change Rule generator for REVAD

Generate IF statement change rules from pull request for Java

## Environment

### OS

Executed on Mac OS(10.13.1)

* Python3

Need `PyGitHub`

```sh
pip3 install PyGithub
```

* R
  * package:apriori

```sh
R
> install.packages('arules')
```

## Usage

### Argument

* apiurl: URL of GitHub or GitHub Enterprise API(e.g. <https://api.github.com> or <http(s)://hostname/api/v3>)
* user: GitHub user Id
* password: GitHub user password
* owner: Project owner Id
* project: Project name
* pull_file: Pull file name on step 1
* outdir: Patch file directory for step2

### Clone this repository

```sh
git clone https://github.com/Ikuyadeu/ChangeRuleGenerator.git
cd ChangeRuleGenerator
```

### Collect pull requests and changes data (Python)

* Collect pull requests

```sh
python3 python/RequestPullList.py apiurl user password owner project
```

* Collect patch data

```sh
mkdir outdir
python3 python/GetPatch.py pull_file outdir user password
```

* Extract changed symbol

```sh
python3 python/ExtractChangedSymbols.py outdir
```

### Generate rule(R)

* Run R terminal

```sh
R
```

* Integrate data

```R
> source("r/merge.r", encoding = "UTF-8")
```

* Generate rule by association mining

```R
> source("r/associate.r", encoding = "UTF-8")
```

### Generate Example from each rule

```sh
python3 python/example_from_rules.py proto_rule.csv git_merged.csv rules.csv
```