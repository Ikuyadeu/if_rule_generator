# IF change Rule generator for REVAD

Generate IF statement change rules from pull request for Java

## Algorithm

Rule generator uses [association rule mining algorithm](https://en.wikipedia.org/wiki/Association_rule_learning)

## Rule example

* LHS: Left Hand Side in association rule mining
* RHS: Right Hand Side in association rule mining
* Ori: Original source code example
* Rev: Revised source code example
* Count: Count for a rule
* All)num: All if changes
* Support: Support score mearn (Count / All If changes)
* LHS_Count: Count of LHS frequency
* Confidence: Support / LHS count
* Lift: Lift score on association rule

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

### Arguments

As the follow is used arguments in Rule generator

* owner: Project owner Id (if you want to collect PR on <https://github.com/octocat/Hello-World> owner is octocat)
* project: Project name (e.g. Hello-World)
* user: GitHub user Id to access the GitHub
* password: GitHub user password

### Clone this repository

```sh
git clone https://github.com/Ikuyadeu/ChangeRuleGenerator.git
cd ChangeRuleGenerator
```

### Collect pull requests and changes data (Python)

* Collect pull requests

```sh
mkdir -p `project`/diffs
python3 python/RequestPullList.py https://api.github.com `owner` `project` `user` `password`
```

* Collect diff url

```sh
python3 python/RequestDiffList.py `owner` `project` `user` `password`
```

* Collect patch data

```sh
python3 python/GetDiffs.py `project` `user` `password`
```

* Extract changed symbol

```sh
python3 python/ExtractChangedSymbols.py `project`
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

Quit the R session

```sh
python3 python/example_from_rules.py `project`
```