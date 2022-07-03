
void swap(var v, int i, int j){
  var a = v[i];
  v[i] = v[j];
  v[j] = a;
}

bool comp(var v1, var v2){
  return v1[v1.length-1] < v2[v2.length-1];
}

class PriorityQueueVec{
  var heap;
  var size;
  void buildHeap(initialK){
    heap.add([]);
    for (int i=0; i < initialK.length; i++){
      heap.add(initialK[i]);
    }
    for (int j = initialK.length ~/2; j>0; j--){
      bubbleDown(j);
    }
  }
  PriorityQueueVec(initialK){
    heap = [];
    size = 0;
    buildHeap(initialK);
  }

  void insert(v){
    heap.add(v);
    bubbleUp(heap.length-1);
  }


  void bubbleUp(int i){
    bool work = true;
    int ind = i;
    while (work){
      work = comp(heap[ind],heap[ind~/2]);
      if (work){
        swap(heap,ind ~/2,ind);
        ind = ind ~/ 2;
      }
      if (ind == 0){
        work = false;
      }
    }
  }
  void bubbleDown(int i) {
    int ind = i;
    bool work = true;
    while (2 * ind + 1 < heap.length & work) {
      if (comp(heap[2 * ind], heap[2 * ind + 1])) {
        if (comp(heap[2*ind], heap[ind])){
          swap(heap, ind, 2*ind);
          ind *=2;
        }else {
          work = false;
        }
      }
      else{
        if (comp(heap[2*ind+1], heap[ind])){
          swap(heap, ind, 2*ind+1);
          ind = 2*ind + 1;
        }
        else{
          work = false;
        }
      }
      if (2*ind <heap.length & comp(heap[2*ind], heap[ind])){
        swap(heap, ind, 2*ind);
      }
    }
  }
  List removeMin(){
    var aux = heap[heap.length-1];
    heap.pop();
    var minE = heap[1];
    heap[1] = aux;
    bubbleDown(1);
    return minE;
  }
}