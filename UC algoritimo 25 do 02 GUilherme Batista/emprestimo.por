programa{
    funcao inicio(){
        real pr, sr, pcl, pct
        inteiro ans, mss

        escreva("Qual o valor do imóvel: ")
        leia(pr)

        escreva("Qual o valor do salário mensal do comprador: ")
        leia(sr)

        escreva("Em quantos anos o comprador pretende quitar o imóvel: ")
        leia(ans)

        mss = ans * 12

        pcl = pr / mss

        pct = sr * 0.3

        se(pcl >= pct){
            escreva("Parcelas de ", pcl,"R$ mensais; Sentimos muito, mas o seu emprestimo foi negado, pois, o valor exede 30% do salário do comprador do imovel.")
        }senao{
            escreva("Parcelas de ", pcl,"R$ mensais;Parabéns, O seu Emprestimo foi aprovado.")

        }


    }
}