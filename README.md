# Review Analyzer
O Review Analyzer é um projeto open source com o objetivo de analisar reviews. 

Utilizamos o Kibana como interface de visualização, para guardar os dados usamos o Elasticsearch que é um servidor de buscas distribuído e o Logstash para fazer o processamento dos dados.

Para treinar os nossos modelos usamos as bilbioteca do Tensorflow e a do Scikit Learn.

Fique a vontade para contribuir para o repositório com mais exemplos seja de dados ou de modelos.

## Tecnologias

<img src="https://www.tensorflow.org/images/tf_logo_social.png" alt="Tensorflow" height="100" width="200"/><img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="Python" height="100" width="110"/><img src="https://i0.wp.com/kubedex.com/wp-content/uploads/2018/09/kibana-1.png" alt="Kibana" height="100" width="110"/><img src="https://miro.medium.com/max/892/1*AYP0Mg_MwJMm3Kbx8Xa8lQ.png" alt="ElasticSearch" height="100" width="200"/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit" height="100" width="200"/>

## Utilização

### Utilizando Online
Atualmente não temos um servidor com o nosso ambiente.

### Instalando Localmente
Primeiramente é necessário ter [Docker](https://docs.docker.com/install/) e o [Docker-Compose](https://docs.docker.com/compose/install/). Com eles é possível subir a parte de visualização dos dados.

Para o Web Scrapping e subir os dados no kibana pelo Elasticsearch instale os requirements.txt

### Rodando o Ambiente

Para baixar 

```bash
cd ~/your/directory/
git clone https://github.com/deeplearningunb/review_analyzer.git
cd review_analyzer
```

Para subir os containers do Docker

```bash
docker-compose build
docker-compose up
```

Se tudo deu certo, já é possível utilizar o Kibana entrando no endereço `http://localhost:5601/`. Entrando nele, você verá a interface do Kibana. Acessando `http://localhost:9200/`, você terá acesso ao Elasticsearch.

### Rodando nossas ferramentas

#### Web Scrapping
Para facilitar a analise de sentimento, nós desenvolvemos algumas funções:

O Web Scrapping de reviews de filmes foi criado usando as bibliotecas do Beautiful Soup e do request atualmente ela só suporta o `https://www.rottentomatoes.com/`. 

Para utilizar é necessário criar um arquivo de urls.

```bash
cd web_scrapping
touch nome_do_arquivo_de_urls
vim nome_do_arquivo_de_urls
```

Dentro do arquivo escreva o nome das urls que você quer que seja feito a extração das reviews. Como no exemplo abaixo

```
https://www.rottentomatoes.com/m/black_panther_2018
https://www.rottentomatoes.com/m/mission_impossible_fallout
https://www.rottentomatoes.com/m/blackkklansman
https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse
https://www.rottentomatoes.com/m/roma_2018
```

Depois disso basta passar o arquivo como parâmetro.
```bash
cd web_scrapping
python3 get_review.py nome_do_arquivo_de_urls
```

#### Comunicação Elasticsearch

Para importar os arquivos csv, é necessário fazer várias requisições. Para agilizar esse processo, nós criamos uma função que faz isso para você. Só precisa passar os parâmetros e ela fará o resto.

```bash
cd import_to_kibana
python3 import_csv.py nome_do_arquivo_csv index tipo_doc
```
## Contribuidores

Agradecimentos para essas pessoas maravilhosas ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/cjjcastro"><img src="https://avatars0.githubusercontent.com/u/26393787?v=4" width="100px;" alt="Cleber Júnior" />
                <br /><sub><b>Cleber Júnior</b></sub></a>
            <br /><a href="https://github.com/fga-eps-mds/2019.1-hubcare-docs/commits?author=cjjcastro" title="Code">💻</a></td>
        <td align="center">
            <a href="https://github.com/Hiroshi18"><img src="https://avatars0.githubusercontent.com/u/26282955?v=4" width="100px;" alt="Lucas Hiroshi Horinouchi" />
                <br /><sub><b>Lucas Hiroshi Horinouchi</b></sub></a>
            <br /><a href="https://github.com/fga-eps-mds/2019.1-hubcare-docs/commits?author=Hiroshi18" title="Code">💻</a> <a href="https://github.com/fga-eps-mds/2019.1-hubcare-docs/commits?author=Hiroshi18" title="Documentation">📖</a></td>
        <td align="center">
            <a href="https://github.com/mateusnr"><img src="https://avatars0.githubusercontent.com/u/13491922?v=4" width="100px;" alt="Mateus Nóbrega" />
                <br /><sub><b>Mateus Nóbrega</b></sub></a>
            <br /><a href="https://github.com/fga-eps-mds/2019.1-hubcare-docs/commits?author=mateusnr" title="Code">💻</a></td>
        <td align="center">
            <a href="https://github.com/Lorryaze"><img src="https://avatars1.githubusercontent.com/u/30262806?v=4" width="100px;" alt="Francisco Heronildo" />
                <br /><sub><b>Lorrany Azevedo</b></sub></a>
            <br /><a href="https://github.com/fga-eps-mds/2019.1-hubcare-docs/commits?author=Lorryaze" title="Code">💻</a></td>
    </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

O nosso código e as ferramentas desenvolvidas pela equipe está dentro da [MIT License](./LICENSE), mas as ferramentas externas como o Kibana e o Elastic Search são Apache.
