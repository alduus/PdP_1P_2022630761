;Castillo Reyes Diego
;Escamilla Reséndiz Aldo
;Lopez Sanchez Adair
;Yañez Martinez Marthon Leobardo

(
    defun factorial(num)
        (if(= num 1)
            1
            (* num (factorial(- num 1)))
        )
)


(print (factorial 5))