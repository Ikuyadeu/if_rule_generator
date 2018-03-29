# IF change Rule generator for REVAD

`REVAD/ueda/changecode.js`で使うIF文のルールを生成する．
<!-- Generate IF statement change rules from pull request for using `REVAD/ueda/changecode.js` -->

## Output

以下の内容を`example_rules`として出力する．

* LHS: アソシエーションルールの条件部
* RHS: アソシエーションルールの結論部
* Ori: 変更前のソースコード例
* Rev: 変更後のソースコード例
* Count: ルールが出現する回数
* Support: 支持度 (Count / IFの変更数)
* All_num: IFの変更数
* Confidence: 支持度 (Support / LHS_count)
* LHS_Count: LHSの出現回数
* Lift: リフト値 (Confidence / LHS_Count)

<!-- * LHS: Left Hand Side in association rule mining
* RHS: Right Hand Side in association rule mining
* Ori: Original source code example
* Rev: Revised source code example
* Count: Count for a rule
* Support: Support score mearn (Count / All If changes)
* All_num: All if changes
* Confidence: Support / LHS count
* LHS_Count: Count of LHS frequency
* Lift: Lift score on association rule -->

## Environment

Python, Rそれぞれのパッケージをインストール

* `PyGitHub`:Python3

```sh
pip3 install PyGithub
```

* `apriori`:R

```sh
R
> install.packages('arules')
```

## Usage

### Arguments

ルール生成に利用する引数

<!-- As the follow is used arguments in Rule generator -->

* owner: プロジェクトオーナー名 (e.g. <https://github.com/octocat/Hello-World>の場合は`octocat`)
* project: プロジェクト名 (e.g. Hello-World)
* user: スクリプトを回すユーザーのGitHub ID
* password: 同じくパスワード

<!-- * owner: Project owner Id (if you want to collect PR on <https://github.com/octocat/Hello-World> owner is octocat)
* project: Project name (e.g. Hello-World)
* user: GitHub user Id to access the GitHub
* password: GitHub user password -->

### Clone this repository

このプロジェクトをクローンするすでにローカルで見ている場合は飛ばす

```sh
git clone https://github.com/Ikuyadeu/ChangeRuleGenerator.git
cd ChangeRuleGenerator
```

### Collect pull requests and changes data (Python)

出力はすべて対象プロジェクト名のディレクトリに出される．

* Collect pull requests -> output:`pulls.json`

```sh
mkdir -p `project`/diffs
python3 python/RequestPullList.py https://api.github.com `owner` `project` `user` `password`
```

* Collect diff url -> output:`diffs.csv`

```sh
python3 python/RequestDiffList.py `owner` `project` `user` `password`
```

* Collect patch data -> output:`diffs/`

```sh
python3 python/GetDiffs.py `project` `user` `password`
```

* Extract changed symbol -> output:`git_ori.csv` and `git_rev.csv`

```sh
python3 python/ExtractChangedSymbols.py `project`
```

### Generate rule(R)

* Run R terminal

```sh
R
```

* Integrate data -> output:`git_merged`

```R
> source("r/merge.r", encoding = "UTF-8")
```

* Generate rule by association mining -> output:`rules.csv`

```R
> source("r/associate.r", encoding = "UTF-8")
```

### Generate Example from each rule -> output:`example_rules.csv`

```sh
python3 python/example_from_rules.py `project`
```

You will get `./project/example_rules.csv`.
