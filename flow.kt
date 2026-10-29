

package com.example.particularpractice



class MutableStateFlow<T>(var value: T){
    
    private val Listener = mutableListOf<(T)->Unit>()
    fun update(transformer: (T)->T){
        this.value = transformer(this.value)
        Listener.forEach{it(this.value)
            
        }
    }
    
    fun collect(collector: (T)->Unit) {
        collector(this.value)
        Listener.add(collector)
    }
}


fun main() {
    
    val _taskState = MutableStateFlow(listOf(10, 20, 30))
    
    
    _taskState.collect {
        println("DISPLAYER: $it")
    }
     
    _taskState.update {
        it+40
    }
    _taskState.update {
        it+50
    }
    _taskState.update {
        it+60
    }
    _taskState.update {
        it+70
    }
}
